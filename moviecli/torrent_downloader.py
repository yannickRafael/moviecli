import threading
from torrentp import TorrentDownloader as TPDownloader

class TorrentDownloader:
    def __init__(self, file_path, save_path='.', port=6881, stop_after_download=True, refresh_interval=1):
        self._file_path = file_path
        self._save_path = save_path
        self._port = port  
        self._stop_after_download = stop_after_download
        self._refresh_interval = refresh_interval

        self.torrent = TPDownloader(
            file_path=file_path,
            save_path=save_path,
            port=port,
            stop_after_download=stop_after_download
        )

        self.progress = 0.0
        self._progress_timer = None
        self._downloading = False

    def start_download(self):
        self._downloading = True
        self.torrent.start_download()
        self._start_progress_monitor()

    def pause_download(self):
        self.torrent.pause_download()
        self._downloading = False
        self._cancel_progress_monitor()

    def resume_download(self):
        self.torrent.resume_download()
        self._downloading = True
        self._start_progress_monitor()

    def stop_download(self):
        self.torrent.stop_download()
        self._downloading = False
        self._cancel_progress_monitor()

    def _start_progress_monitor(self):
        self._cancel_progress_monitor()
        self._progress_timer = threading.Timer(self._refresh_interval, self._monitor_progress)
        self._progress_timer.start()

    def _cancel_progress_monitor(self):
        if self._progress_timer:
            self._progress_timer.cancel()
            self._progress_timer = None

    def get_progress(self):
        try:
            return round(self.torrent._downloader._get_status_progress, 2)
        except:
            return self.progress


    def _monitor_progress(self):
        if not self._downloading:
            return

        try:
            self.progress = self.torrent._downloader._get_status_progress
            print(f"Progresso: {self.progress:.2f}%")
        except Exception as e:
            print("Erro ao obter progresso:", e)
            self._downloading = False
            return

        if self.progress >= 100.0:
            print("Download concluído!")
            self._downloading = False
            return

        self._start_progress_monitor()
