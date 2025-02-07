import os
import random
import yt_dlp

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:110.0) Gecko/20100101 Firefox/110.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.92 Mobile Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
]

def banner():
    os.system("clear")
    print("\033[91m" + """
▓██   ██▓▄▄▄█████▓ ██▀███   █    ██ ▓█████▄ ▓█████  ██▀███
 ▒██  ██▒▓  ██▒ ▓▒▓██ ▒ ██▒ ██  ▓██▒▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒
  ▒██ ██░▒ ▓██░ ▒░▓██ ░▄█ ▒▓██  ▒██░░██   █▌▒███   ▓██ ░▄█ ▒
  ░ ▐██▓░░ ▓██▓ ░ ▒██▀▀█▄  ▓▓█  ░██░░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄
  ░ ██▒▓░  ▒██▒ ░ ░██▓ ▒██▒▒▒█████▓ ░▒████▓ ░▒████▒░██▓ ▒██▒
   ██▒▒▒   ▒ ░░   ░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒  ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
 ▓██ ░▒░     ░      ░▒ ░ ▒░░░▒░ ░ ░  ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░
 ▒ ▒ ░░    ░        ░░   ░  ░░░ ░ ░  ░ ░  ░    ░     ░░   ░
 ░ ░                 ░        ░        ░       ░  ░   ░
 ░ ░                                 ░
    """ + "\033[0m")
    print("\n      \033[91mAuthor: g0w6y\033[0m")

OUTPUT_DIR = "output"
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)


def download_youtube_video(url, mode):
    try:
        user_agent = random.choice(USER_AGENTS)

        format_select = {
            "video": "bestvideo+bestaudio/best",
            "shorts": "bestvideo+bestaudio/best",
            "live": "best",
            "audio": "bestaudio"
        }.get(mode, "bestvideo+bestaudio/best")

        postprocessors = [
            {'key': 'FFmpegMerger'}
        ] if mode != "audio" else [
            {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}
        ]

        options = {
            'outtmpl': f"{OUTPUT_DIR}/%(title)s.%(ext)s",
            'merge_output_format': 'mp4',
            'format': format_select,
            'postprocessors': postprocessors,
            'http_headers': {'User-Agent': user_agent},
            'noprogress': True, 
            'quiet': False,
            'noplaylist': True 
        }

        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])

        print("\n\033[92mDownload Complete! File saved in 'output' directory.\033[0m\n")

    except Exception as e:
        print(f"\n\033[91mError: {e}\033[0m\n")

def main():
    banner()
    while True:
        print("\n\033[96m[1]\033[0m Download Live Stream")
        print("\033[96m[2]\033[0m Download Normal Video")
        print("\033[96m[3]\033[0m Download YouTube Shorts")
        print("\033[96m[4]\033[0m Download Audio Only")
        print("\033[96m[5]\033[0m Exit")

        choice = input("\n\033[93mEnter your choice:\033[0m ")

        if choice in ["1", "2", "3", "4"]:
            url = input("\n\033[94mEnter YouTube URL: \033[0m")

            if choice == "1":
                print("\n\033[92mDownloading Live Stream...\033[0m")
                download_youtube_video(url, "live")

            elif choice == "2":
                print("\n\033[92mDownloading Normal Video...\033[0m")
                download_youtube_video(url, "video")

            elif choice == "3":
                print("\n\033[92mDownloading YouTube Shorts...\033[0m")
                download_youtube_video(url, "shorts")

            elif choice == "4":
                print("\n\033[92mDownloading Audio Only...\033[0m")
                download_youtube_video(url, "audio")

        elif choice == "5":
            print("\n\033[91mExiting Ytruder...\033[0m\n")
            break

        else:
            print("\n\033[91mInvalid choice! Try again.\033[0m\n")

if __name__ == "__main__":
    main()
    
