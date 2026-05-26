#!/usr/bin/env python3
"""
职场英语每日对话 → 音频生成器
使用 Edge-TTS（微软免费）将对话转换为音频

用法：
  python3 generate_audio.py day-03/dialogue.md
  python3 generate_audio.py --all
"""

import asyncio
import argparse
import os
import re
import shutil
import tempfile
from pathlib import Path

# 声音配置
VOICE_MAP = {
    "A": "en-US-AriaNeural",        # 女声 - 自信
    "B": "en-US-BrianNeural",       # 男声 - 随意真诚
    "C": "en-US-EmmaNeural",        # 女声 - 开朗
    "D": "en-US-ChristopherNeural", # 男声 - 权威
}

BASE_DIR = Path(__file__).parent.parent

def clean_text(text: str) -> str:
    """清理 markdown 标记和特殊符号"""
    # 去掉加粗标记
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    # 去掉语调箭头
    text = re.sub(r'[↗↘↔→]', '', text)
    # 去掉 emoji
    text = re.sub(r'[\U0001F300-\U0001F9FF]', '', text)
    # 去掉多余的空格
    text = re.sub(r'\s+', ' ', text).strip()
    return text

async def generate_dialogue_audio(dialogue_path: str, output_path: str = None):
    """从 dialogue.md 生成完整对话音频"""
    import edge_tts
    
    content = Path(dialogue_path).read_text(encoding="utf-8")
    lines = content.split("\n")
    
    temp_dir = tempfile.mkdtemp()
    audio_segments = []
    segment_idx = 0
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # 匹配说话人
        speaker_match = re.match(r'^([A-D])\s*(?:[（(][^）)]*[）)])?\s*[:：]\s*(.+?)(?:\s*>\s*.+)?$', line)
        
        if speaker_match:
            speaker = speaker_match.group(1)
            text = speaker_match.group(2).strip()
            
            # 去掉中文翻译（> 后面的部分已在正则中处理，但保险起见再处理一次）
            text = re.sub(r'\s*>\s*.*$', '', text).strip()
            
            if not text or len(text) < 3:
                continue
            
            # 纯中文行跳过
            if re.match(r'^[\u4e00-\u9fff\s\d，。！？、：；""''（）【】]+$', text):
                continue
            
            # 清理 markdown 标记
            text = clean_text(text)
            
            if not text:
                continue
            
            voice = VOICE_MAP.get(speaker, VOICE_MAP["A"])
            seg_path = os.path.join(temp_dir, f"seg_{segment_idx:04d}.mp3")
            
            try:
                communicate = edge_tts.Communicate(text, voice, rate="-5%")
                await communicate.save(seg_path)
                audio_segments.append(seg_path)
                segment_idx += 1
                print(f"  ✅ {speaker}: {text[:60]}")
            except Exception as e:
                print(f"  ❌ 失败: {e}")
    
    if not audio_segments:
        print("⚠️ 没有找到可生成的对话内容")
        return None
    
    if output_path is None:
        day_dir = Path(dialogue_path).parent.name
        output_path = str(BASE_DIR / day_dir / "dialogue.mp3")
    
    # 生成 0.8 秒停顿
    silence_path = os.path.join(temp_dir, "silence.mp3")
    os.system(f"ffmpeg -y -f lavfi -i anullsrc=r=24000:cl=mono -t 0.8 -q:a 9 {silence_path} 2>/dev/null")
    
    # 交叉排列：对话 + 停顿
    interleaved_list = os.path.join(temp_dir, "interleaved.txt")
    with open(interleaved_list, 'w') as f:
        for seg in audio_segments:
            f.write(f"file '{seg}'\n")
            f.write(f"file '{silence_path}'\n")
    
    os.system(f"ffmpeg -y -f concat -safe 0 -i {interleaved_list} -c copy {output_path} 2>/dev/null")
    
    shutil.rmtree(temp_dir, ignore_errors=True)
    
    if os.path.exists(output_path):
        size_kb = os.path.getsize(output_path) / 1024
        duration_s = len(audio_segments) * 4  # 粗略估算
        print(f"\n🎧 音频已生成: {output_path}")
        print(f"   大小: {size_kb:.0f} KB | 段数: {len(audio_segments)}")
        return output_path
    else:
        print("❌ 合并失败")
        return None


def main():
    parser = argparse.ArgumentParser(description="职场英语每日对话 → 音频")
    parser.add_argument("input", nargs="?", help="dialogue.md 路径")
    parser.add_argument("--all", action="store_true", help="生成所有 Day 的音频")
    parser.add_argument("--output", "-o", help="输出路径")
    args = parser.parse_args()
    
    if args.all:
        for day_dir in sorted(BASE_DIR.glob("day-*")):
            dialogue = day_dir / "dialogue.md"
            if dialogue.exists():
                output = day_dir / "dialogue.mp3"
                if output.exists():
                    print(f"⏭️ {day_dir.name} 已有音频，跳过")
                    continue
                print(f"\n📝 处理 {day_dir.name}...")
                asyncio.run(generate_dialogue_audio(str(dialogue)))
    elif args.input:
        dialogue_path = args.input
        if not dialogue_path.startswith("/"):
            dialogue_path = str(BASE_DIR / dialogue_path)
        asyncio.run(generate_dialogue_audio(dialogue_path, args.output))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
