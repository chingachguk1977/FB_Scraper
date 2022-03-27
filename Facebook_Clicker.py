import json
import os
import shutil
import time
import webbrowser
import ctypes
import os

import pyautogui
from pynput.keyboard import Key, Controller
from image_search.imagesearch import imagesearch_loop, imagesearch, many_imagesearch


class Facebook_Clicker:
    def __init__(self):
        self.keyboard = Controller()
        self.set_screen_specifics()
        self.latest_capture_position = 0
        self.image_seq = 1
        user32 = ctypes.windll.user32
        self.screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        print(self.screensize)
        self.scroll_speed = self.screensize[1] // 10

    def set_screen_specifics(self):
        #sets screen area to be captured
        alexey = True
        if alexey:
            self.screen_box = (450, 200, 580, 850)
            self.image_save_folder = "c:\\FB_images\\"
        else:
            self.screen_box = (500, 200, 1200, 1000)
            self.image_save_folder = "c:\\FB_images\\"

    def open_browser(self, url):
        chrome_path = '"c:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" '
        os.system(chrome_path + url)

    def scan_channel(self, channel_url, cycles = 5000):
        self.open_browser(channel_url)
        time.sleep(5)


        cwd = os.getcwd()
        print(cwd)

        self.total_scroll = 0
        for n in range(cycles):
            self.scroll_page(n)

    def scroll_page(self, n):
        c = 0
        while True:
            c += 1
            pos = many_imagesearch(["img/more_in_title.png"])
            if pos[1] > 0:
                y_limit = pos[1] + 30
            else:
                y_limit = 0
            print(y_limit)

            pos = many_imagesearch(["img/all_rus.png"], y_limit)
            if pos[1] < 0 or c > 50:
                break
            self.click_pos(pos)

        self.scroll_screen(self.screensize[1] // 10)

        """
        c = 0
        while True:
            c += 1

            pos = many_imagesearch(["img/new_first_rus.png", "img/more_in_title.png"])
            if pos[1] > 0:
                y_limit = pos[1] + 30
            else:
                y_limit = 0
            print(y_limit)

            pos = many_imagesearch(["img/comments_rus.png",
                                    "img/has_answered_rus.png", "img/has_answered2_rus.png",
                                    "img/has_answered3_rus.png", "img/show_more_rus.png"], y_limit)
            if pos[0] < 0 or c > 50:
                break

            pos = many_imagesearch(["img/has_answered_rus.png", "img/has_answered2_rus.png",
                                    "img/has_answered3_rus.png", "img/show_more_rus.png"], y_limit)

            if pos[1] > 0:
                self.click_pos(pos)

            pos = many_imagesearch(["img/comments_rus.png"], y_limit)
            if pos[1] > 0:
                self.click_pos(pos)

            self.scroll_screen(self.screensize[1] // 25)
        """
        self.scroll_screen(self.scroll_speed)

    def click_pos(self, pos):
        pyautogui.moveTo(pos[0] + 10, pos[1] + 10)
        time.sleep(0.2)
        pyautogui.click(button="left")
        time.sleep(0.4)
        pyautogui.moveTo(20, self.screensize[1] // 2)
        time.sleep(0.2)

    def scroll_screen(self, scroll):
        pyautogui.moveTo(20, self.screensize[1] // 2)
        self.total_scroll += scroll
        pyautogui.scroll(-scroll)


        if self.total_scroll - self.latest_capture_position > 500:
            self.capture_screen()
            self.latest_capture_position = self.total_scroll

    def capture_screen(self):
        im = pyautogui.screenshot(region=self.screen_box)
        seq_str = ('00000' + str(self.image_seq))[-5:]
        fname = f'{self.image_save_folder}scr_{seq_str}.png'
        im.save(fname)
        self.image_seq += 1


    """

    def next_next_next_done(self):
        if not self.wait_for_image("images/next_rus.png"):
            time.sleep(50)
            if not self.wait_for_image("images/next_rus.png"):
                return False
        pos = imagesearch("images/next_rus.png")
        if pos[0] == -1:
            return False
        pyautogui.moveTo(pos[0] + 15, pos[1] + 15)
        time.sleep(0.2)
        pyautogui.click(button="left")
        time.sleep(5)
        pyautogui.moveTo(100, 100)
        #self.pr(Key.enter)
        if not self.wait_for_image("images/next_rus.png"):
            time.sleep(50)
            if not self.wait_for_image("images/next_rus.png"):
                return False
        pos = imagesearch("images/next_rus.png")
        if pos[0] == -1:
            return False
        pyautogui.moveTo(pos[0] + 15, pos[1] + 15)
        time.sleep(0.2)
        pyautogui.click(button="left")
        time.sleep(5)
        pyautogui.moveTo(100, 100)
        #self.pr(Key.enter)
        if not self.wait_for_image("images/next_rus.png"):
            time.sleep(50)
            if not self.wait_for_image("images/next_rus.png"):
                return False
        pos = imagesearch("images/next_rus.png")
        if pos[0] == -1:
            return False
        pyautogui.moveTo(pos[0] + 15, pos[1] + 15)
        time.sleep(0.2)
        pyautogui.click(button="left")
        #self.pr(Key.enter)
        time.sleep(7)
        pyautogui.moveTo(100, 100)
        #self.shift_tab_n(3)
        #self.tab_n(1)
        #self.pr(Key.down)
        self.pr(Key.down)
        self.pr(Key.down)
        #self.shift_tab_n(8)
        time.sleep(1)
        #self.pr(Key.enter)
        #time.sleep(6)
        #self.shift_tab_n(1)
        if not self.wait_for_image("images/publish_rus.png"):
            return False
        if pos[0] == -1:
            return False
        pos = imagesearch("images/publish_rus.png")
        pyautogui.moveTo(pos[0] + 15, pos[1] + 15)
        time.sleep(0.2)
        pyautogui.click(button="left")
        time.sleep(5)
        pyautogui.moveTo(100, 100)
        #self.pr(Key.enter)
        return True

    def pr(self, key):
        self.keyboard.press(key)
        self.keyboard.release(key)

    def shift_tab_n(self, n):
        self.keyboard.press(Key.shift)
        for _ in range(n):
            time.sleep(0.3)
            self.keyboard.press(Key.tab)
            self.keyboard.release(Key.tab)
        self.keyboard.release(Key.shift)

    def tab_n(self, n):
        for _ in range(n):
            time.sleep(0.3)
            self.keyboard.press(Key.tab)
            self.keyboard.release(Key.tab)

    def upload_from_info_file(self, url_upload, repeat, from_folder, to_folder):
        self.info_for_upload = []
        fails = 0
        max_fails = 8
        for file_name in os.listdir(from_folder):
            if file_name.lower().endswith(".inf"):
                full_info_file = os.path.join(from_folder, file_name)
                created_date = os.path.getctime(full_info_file)
                with open(full_info_file, 'r', encoding="utf-8") as the_file:
                    info_back = json.load(the_file)
                    info_back['created_date'] = created_date
                    request_body = info_back['request_body']
                    video_file_name = info_back['video_file_name']
                    info_back['info_file_name'] = full_info_file
                    status = request_body['status']
                    self.info_for_upload.append(info_back)
                    the_file.close()

        self.info_for_upload = sorted(self.info_for_upload, key=lambda info_back: info_back['created_date'])

        i = 0
        for info_back in self.info_for_upload:
            if i >= repeat:
                break
            video_file_name = info_back['video_file_name']
            if not os.path.exists(video_file_name):
                continue
            i += 1
            fail = False
            if not self.upload_one_video(info_back, url_upload, video_file_name):
                fail = True
            if not self.wait_for_any_image(["images\\video_published_rus.png", "images\\processing_video_rus.png"]):
                fail = True
            if fail:
                fails += 1
            if fail and fails < max_fails:
                print(f'fail: {video_file_name}')
                time.sleep(30)
                continue

            print(video_file_name)

            full_info_file = info_back['info_file_name']
            #shutil.move(full_info_file, to_folder)
            filename = os.path.basename(full_info_file)
            dest = os.path.join(to_folder, filename)
            if os.path.exists(dest):
                os.remove(dest)
            shutil.move(full_info_file, dest)

            time.sleep(20)

            pass

    def upload_one_video_old(self, info_back, url_upload, video_file_name):
        self.open_browser(url_upload)
        time.sleep(5)
        self.keyboard = Controller()
        self.shift_tab_n(4)
        self.pr(Key.enter)
        time.sleep(5)
        self.type(video_file_name)
        self.pr(Key.enter)
        time.sleep(4)
        self.type(info_back['request_body']['snippet']['title'])
        self.tab_n(2)
        description = info_back['request_body']['snippet']['description']
        for s in description.split("\n"):
            self.type(s)
            time.sleep(0.1)
            self.pr(Key.enter)
        self.tab_n(13)
        self.pr(Key.enter)
        time.sleep(1)
        self.tab_n(6)
        time.sleep(1)
        tags = info_back['request_body']['snippet']['tags']
        for tag in tags:
            self.type(tag)
            self.pr(",")
            time.sleep(0.1)
        self.tab_n(20)
        time.sleep(0.5)
        # self.shift_tab_n(28 + len(tags))
        # time.sleep(3)
        # pass
        # time.sleep(20)
        # self.tab_n(4)
        # next next next
        self.next_next_next_done()
        time.sleep(2)

    def upload_one_video(self, info_back, url_upload, video_file_name):
        self.open_browser(url_upload)
        if not self.wait_for_image("images/select_files_rus.png"):
            return False
        time.sleep(5)
        self.keyboard = Controller()
        self.shift_tab_n(4)
        self.pr(Key.enter)
        time.sleep(5)
        self.type(video_file_name)
        self.pr(Key.enter)
        time.sleep(4)

        #file_size = os.path.getsize(video_file_name)
        #if file_size > 10000000:
        #    time.sleep(30)
        #    for _ in range(file_size // 10000000 + 1):
        #        time.sleep(30)

        self.type(info_back['request_body']['snippet']['title'])
        self.tab_n(2)
        description = info_back['request_body']['snippet']['description']
        for i, s in enumerate(description.split("\n")):
            self.type(s)
            time.sleep(0.1)
            self.pr(Key.enter)
            if i % 20 == 0:
                time.sleep(5)
        self.tab_n(13)
        self.pr(Key.enter)
        time.sleep(1)
        self.tab_n(6)
        time.sleep(1)

        tags = info_back['request_body']['snippet']['tags']
        for tag in tags:
            self.type(tag)
            self.pr(",")
            time.sleep(0.1)
        #self.tab_n(20)
        time.sleep(0.5)
        self.tab_n(1)

        if not self.next_next_next_done():
            return False
        time.sleep(2)
        return True

    def wait_for_any_image(self, img_list):
        found = False
        for _ in range(20):
            for img in img_list:
                pos = imagesearch(img)
                if pos[0] < 0:
                    continue
                found = True
                break
            if found:
                break
            time.sleep(1)
        return found

    def wait_for_image(self, img):
        found = False
        for _ in range(50):
            pos = imagesearch(img)
            if pos[0] < 0:
                time.sleep(1)
                continue
            found = True
            break
        return found

    def type(self, video_file_name):
        for c in video_file_name:
            self.pr(c)

    def upload_from_info_file2(self, url_upload, param, param1, param2):
        pass





    """

