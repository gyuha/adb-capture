import subprocess
import time
import os
import signal
import subprocess


class ScrCpyCapture():
    def start(self, executable_file, cwd='./'):
        return subprocess.Popen(
            executable_file,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=cwd
        )

    def read(self, process):
        return process.stdout.readline().decode("utf-8").strip()

    def write(self, process):
        process.stdin.write('\x03'.encode())
        process.stdin.flush()

    def send_keyboard_interrupt(self, proc):
        """
        Sends a KeyboardInterrupt to the specified child process.
        """
        try:
            # Send KeyboardInterrupt to self, and therefore, to child processes
            try:
                # os.kill(proc.pid, signal.CTRL_C_EVENT)
                # os.kill(0, signal.CTRL_C_EVENT)
                proc.send_signal(signal.CTRL_C_EVENT)
            except AttributeError as e:
                print(e)
            # Immediately throws KeyboardInterrupt from the simulated CTRL-C
            proc.terminate()
            proc.wait(timeout=2)
        except KeyboardInterrupt:
            # Ignore the simulated CTRL-C
            pass

    def terminate(self, process):
        process.stdin.close()
        process.terminate()
        process.wait(timeout=1)

    def capture(self, output):
        p = self.start(['scrcpy', '-Nr', os.path.realpath('tmp.mkv')],
                       os.path.realpath('./bin/scrcpy'))
        time.sleep(1)
        print(output)
        self.send_keyboard_interrupt(p)
        print(output, "> capture")
        p = self.start([os.path.realpath('./bin/ffmpeg/ffmpeg.exe'),
                       '-i', os.path.realpath('tmp.mkv'), '-vframes', '1', os.path.realpath(output)])
        print(output, "> end")
        # os.remove(os.path.realpath('tmp.mkv'))


if __name__ == "__main__":
    scrcpy = ScrCpyCapture()

    scrcpy.capture('1.jpg')
    scrcpy.capture('2.jpg')
