import time
import csv
import pandas as pd 

from selenium import webdriver

channels = [
    'https://youtube.com/@therealpartyyeep?si=nTwENmP7KeCl3X-z/videos',
    ]
urls = {}

class ReportBot():


    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

    def retrieve_link(self):
        channelCount = 0
        totalVideo = 0
        for channel in channels:
            channelCount += 1
            self.driver.get(channel)
            videos = self.driver.find_elements_by_id('video-title')
            
            videoCount = 0 

            for video in videos:
                url = video.get_attribute("href")
                temp_video_name = video.text
                video_name = temp_video_name.encode('utf-8')
                urls[video_name] = url[32:]
                videoCount += 1
                print('Video Processed: {}'.format(videoCount))
                time.sleep(2)
                
                
            totalVideo += videoCount
            print('{} channel(s) processed\n {} videos processed.'.format(channelCount, videoCount))
        
        
        
        df = pd.DataFrame(urls.items())

        

        print('All video processed, total number of video = {}'.format(totalVideo))
        df = df.rename(columns = {"0" : "VideoTitle", "1": "videoId"})
        df.to_csv('output.csv', index=False)
        print('File compiled')

if __name__ == "__main__":
    bot = ReportBot()
    bot.retrieve_link()
