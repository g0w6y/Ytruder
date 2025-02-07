
# **Ytruder - YouTube Video & Audio Downloader**  

**Ytruder** is a powerful YouTube downloader tool built using **yt-dlp**. It supports downloading:  
✅ Live Streams  
✅ Normal Videos  
✅ YouTube Shorts  
✅ Audio Only  

## **Features**  
- Random **User-Agent Spoofing** for better request handling.  
- Supports **MP4** and **MP3** formats.  
- **Merges audio & video** automatically.  
- **Simple & Interactive** menu-driven CLI.  

---

## **Installation**  

### **1. Install Dependencies**  
Make sure you have **Python 3** installed. Then, install `yt-dlp`:  

```sh
pip install yt-dlp
```

You'll also need **FFmpeg** for processing media files:  

- **Linux (Debian/Ubuntu)**:  
  ```sh
  sudo apt install ffmpeg
  ```
- **MacOS (Homebrew)**:  
  ```sh
  brew install ffmpeg
  ```
- **Windows**: Download and install FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html).  

---

## **Usage**  

### **Run the script**  
```sh
python ytruder.py
```

### **Select an option:**  
1️⃣ Download **Live Stream**  
2️⃣ Download **Normal Video**  
3️⃣ Download **YouTube Shorts**  
4️⃣ Download **Audio Only**  
5️⃣ **Exit**  

---

## **Output Files**  
All downloaded files are saved inside the **`output/`** folder.  

---

## **Example Usage**  
#### **Download a YouTube Video**  
```sh
Enter your choice: 2  
Enter YouTube URL: https://www.youtube.com/watch?v=VIDEO_ID  
Downloading Normal Video...
```

#### **Download Audio Only**  
```sh
Enter your choice: 4  
Enter YouTube URL: https://www.youtube.com/watch?v=VIDEO_ID  
Downloading Audio Only...
```

---

## **Troubleshooting**  
🔴 **"yt-dlp command not found"** → Run `pip install --upgrade yt-dlp`  
🔴 **FFmpeg missing error** → Install FFmpeg as shown above.  
🔴 **Error downloading video?** → Try another User-Agent or check the URL.  

---

## **Author**  
👤 **g0w6y**  

⚠️ **Use responsibly and comply with YouTube's terms.**  
