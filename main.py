from os import rename
# import youtube_dl
import yt_dlp
import ffmpeg

def download(youtube_url):
    # 定义某些下载参数
    ydl_opts = {
        # outtmpl 格式化下载后的文件名，避免默认文件名太长无法保存
        'outtmpl': '%(title)s.f%(format_id)s.%(ext)s',
        # 'simulate': 'simulate',
        'format': 'bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4] / bv*+ba/b',
        'no_warnings': 'no_warnings',

    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

if __name__ == '__main__':
    download('https://www.bilibili.com/video/BV1sT411N7jY/?spm_id_from=333.1007.tianma.1-3-3.click')