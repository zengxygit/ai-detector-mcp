#!/usr/bin/env python3
"""
示例使用脚本 - 演示如何使用AI检测MCP服务
"""

import asyncio
import json


async def example_image_detection():
    """图像检测示例"""
    print("\n=== 图像检测示例 ===")
    result = {
        "status": "success",
        "file": "example.jpg",
        "model_used": "DINOv2",
        "is_ai_generated": 0.32,
        "is_manipulated": 0.18,
        "confidence": 0.94,
        "details": {
            "feature_anomaly_score": 0.32,
            "texture_consistency": 0.95
        }
    }
    print(f"结果: {json.dumps(result, ensure_ascii=False, indent=2)}")
    return result


async def example_video_detection():
    """视频检测示例"""
    print("\n=== 视频检测示例 ===")
    result = {
        "status": "success",
        "file": "example.mp4",
        "model_used": "DINOv2 for Video",
        "total_frames_analyzed": 5,
        "summary": {
            "average_deepfake_score": 0.35,
            "max_deepfake_score": 0.45,
            "min_deepfake_score": 0.25,
            "overall_verdict": "possibly_fake",
            "risk_level": "low"
        }
    }
    print(f"结果: {json.dumps(result, ensure_ascii=False, indent=2)}")
    return result


async def example_audio_detection():
    """音频检测示例"""
    print("\n=== 音频检测示例 ===")
    result = {
        "status": "success",
        "file": "example.mp3",
        "model_used": "Vocoder Artifact Detection",
        "is_synthetic": 0.42,
        "cloning_probability": 0.38,
        "confidence": 0.89
    }
    print(f"结果: {json.dumps(result, ensure_ascii=False, indent=2)}")
    return result


async def example_text_detection():
    """文本检测示例"""
    print("\n=== 文本检测示例 ===")
    result = {
        "status": "success",
        "model_used": "RoBERTa Classifier",
        "text_length": 150,
        "word_count": 30,
        "is_ai_generated": 0.65,
        "probability": 0.65,
        "confidence": 0.89,
        "ai_markers": [
            {"marker": "首先", "type": "常见的结构性开头", "frequency": 1}
        ]
    }
    print(f"结果: {json.dumps(result, ensure_ascii=False, indent=2)}")
    return result


if __name__ == "__main__":
    asyncio.run(example_image_detection())
    asyncio.run(example_video_detection())
    asyncio.run(example_audio_detection())
    asyncio.run(example_text_detection())
