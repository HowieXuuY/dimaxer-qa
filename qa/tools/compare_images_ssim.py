"""SSIM image compare for ImGui capture baselines (requires OpenCV cv2 on PYTHONPATH)."""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path


def _compute_ssim(img1, img2):
    import cv2
    import numpy as np

    c1 = (0.01 * 255) ** 2
    c2 = (0.03 * 255) ** 2

    img1_f = img1.astype(np.float64)
    img2_f = img2.astype(np.float64)

    mu1 = cv2.GaussianBlur(img1_f, (11, 11), 1.5)
    mu2 = cv2.GaussianBlur(img2_f, (11, 11), 1.5)

    mu1_sq = mu1 * mu1
    mu2_sq = mu2 * mu2
    mu1_mu2 = mu1 * mu2

    sigma1_sq = cv2.GaussianBlur(img1_f * img1_f, (11, 11), 1.5) - mu1_sq
    sigma2_sq = cv2.GaussianBlur(img2_f * img2_f, (11, 11), 1.5) - mu2_sq
    sigma12 = cv2.GaussianBlur(img1_f * img2_f, (11, 11), 1.5) - mu1_mu2

    numerator = (2 * mu1_mu2 + c1) * (2 * sigma12 + c2)
    denominator = (mu1_sq + mu2_sq + c1) * (sigma1_sq + sigma2_sq + c2)
    ssim_map = np.divide(numerator, denominator, out=np.zeros_like(numerator), where=denominator != 0)
    return float(ssim_map.mean())


def compare_images(
    baseline: str,
    actual: str,
    *,
    threshold: float = 0.99,
    wait_seconds: float = 1.0,
) -> tuple[bool, str]:
    import cv2

    baseline_path = Path(baseline)
    actual_path = Path(actual)

    deadline = time.monotonic() + max(0.0, wait_seconds)
    while time.monotonic() < deadline:
        if actual_path.is_file():
            break
        time.sleep(0.01)
    if not actual_path.is_file():
        detail = f"actual file not ready: {actual}"
        print(f"compare_images_ssim: {detail}", file=sys.stderr)
        return False, detail

    img1 = cv2.imread(str(baseline_path), cv2.IMREAD_COLOR)
    img2 = cv2.imread(str(actual_path), cv2.IMREAD_COLOR)
    if img1 is None or img2 is None:
        detail = f"failed to read images baseline={baseline} actual={actual}"
        print(f"compare_images_ssim: {detail}", file=sys.stderr)
        return False, detail
    if img1.shape != img2.shape:
        detail = f"size mismatch {img1.shape} vs {img2.shape}"
        print(f"compare_images_ssim: {detail}", file=sys.stderr)
        return False, detail

    channels = img1.shape[2] if img1.ndim == 3 else 1
    if channels >= 3:
        scores = [_compute_ssim(img1[:, :, c], img2[:, :, c]) for c in range(3)]
        avg_ssim = sum(scores) / len(scores)
    else:
        avg_ssim = _compute_ssim(img1, img2)

    ok = avg_ssim >= threshold
    detail = f"SSIM={avg_ssim:.6f} threshold={threshold:.4f} -> {'PASS' if ok else 'FAIL'}"
    print(detail)
    return ok, detail


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Compare two PNG captures via SSIM.")
    parser.add_argument("baseline")
    parser.add_argument("actual")
    parser.add_argument("--threshold", type=float, default=0.99)
    parser.add_argument("--wait-seconds", type=float, default=1.0)
    ns = parser.parse_args(argv)
    ok, detail = compare_images(ns.baseline, ns.actual, threshold=ns.threshold, wait_seconds=ns.wait_seconds)
    if not ok and detail:
        print(detail, file=sys.stderr)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
