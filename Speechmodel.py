from aip import AipSpeech
'''百度语言识别模块'''
class Translation(object):
    def __init__(self,app_id,api_key,secret_ket):
        """  APPID AK SK """
        APP_ID = app_id
        API_KEY = api_key
        SECRET_KEY = secret_ket
        self.cliten = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    def __get_file_stream(sele,filepath):
        with open(filepath,'rb') as f:
            return f.read()
    def get_words(self,filepath):
        req=self.cliten.asr(self.__get_file_stream(filepath),'wav',16000,{'dev_pid': '1537',})
        print(req)
if __name__ == '__main__':
    translation=Translation('11028406','EB33m8by59KYPtxW2zgbG5FO','******************* ')
    translation.get_words('output.wav')