import sys
import yt_dlp
from yt_dlp.postprocessor.metadataparser import MetadataParserPP

def download_music(mode, url):
    # Base template: Artist - CleanedTitle.opus
    outtmpl = './%(artist,uploader)s - %(title)s.%(ext)s'
    
    if mode == 'playlist':
        noplaylist = False
    else:
        noplaylist = True

    # Regex matching common YouTube fluff inside parentheses/brackets
    # Matches: (Official Audio), [Official Music Video], (Lyrics), (Visualizer), [4K], etc.
    junk_pattern = (
        r'(?i)\s*[\(\[]\s*'
        r'(?:official\s+(?:audio|video|music\s+video|lyric\s+video|visualizer|clip)|'
        r'lyrics?|audio|visualizer|music\s+video|video\s+clip|'
        r'4k|hd|hq|remastered|explicit)'
        r'\s*[\)\]]'
    )

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': outtmpl,
        'ignoreerrors': True,
        'noplaylist': noplaylist,
        'overwrites': True,

        'postprocessors': [
            # 1. Strip junk from title before processing filename or tags
            {
                'key': 'MetadataParser',
                'when': 'pre_process',
                'actions': [
                    (MetadataParserPP.Actions.REPLACE, 'title', junk_pattern, ''),
                ],
            },
            # 2. Extract and encode audio to Opus
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'opus',
            },
            # 3. Write metadata (uses the cleaned-up title)
            {
                'key': 'FFmpegMetadata',
                'add_metadata': True,
            },
            # 4. Prepare and attach album art
            {
                'key': 'FFmpegThumbnailsConvertor',
                'format': 'png',
            },
            {
                'key': 'EmbedThumbnail',
            },
        ],
        'writethumbnail': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Error: Invalid arguments.")
        print("Usage: python getmusic.py [single|playlist] <URL>")
        sys.exit(1)

    mode = sys.argv[1].lower()
    url = sys.argv[2]

    if mode not in ['single', 'playlist']:
        print("Error: First argument must be exactly 'single' or 'playlist'.")
        sys.exit(1)

    is_playlist_url = 'list=' in url or '/playlist' in url

    if mode == 'single' and is_playlist_url:
        print("Error: You specified 'single', but provided a playlist URL (contains 'list=' or '/playlist').")
        sys.exit(1)

    if mode == 'playlist' and not is_playlist_url:
        print("Error: You specified 'playlist', but provided a single track URL (missing 'list=').")
        sys.exit(1)

    download_music(mode, url)
