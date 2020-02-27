from kalliope.core import FileManager
from kalliope.core.TTS.TTSModule import TTSModule, FailToLoadSoundFile, MissingTTSParameter
import logging

import boto3

logging.basicConfig()
logger = logging.getLogger("kalliope")


class Pollytts(TTSModule):
    def __init__(self, **kwargs):
        super(Pollytts, self).__init__(**kwargs)
        self.voice = kwargs.get('voice', 'Ivy')
        self.aws_access_key_id = kwargs.get('aws_access_key_id', None)
        self.aws_secret_access_key = kwargs.get('aws_secret_access_key', None)
        self.region_name = kwargs.get('region_name', 'eu-west-2 ')

        self._check_parameters()

    def say(self, words):
        """
        :param words: The sentence to say
        """

        self.generate_and_play(words, self._generate_audio_file)

    def _check_parameters(self):
        """
        Check parameters are ok, raise MissingTTSParameterException exception otherwise.
        :return: true if parameters are ok, raise an exception otherwise

               .. raises:: MissingTTSParameterException
        """
        if self.aws_access_key_id is None:
            raise MissingTTSParameter("[PollyTTS] Missing aws_access_key_id")
        if self.aws_secret_access_key is None:
            raise MissingTTSParameter("[PollyTTS] Missing aws_secret_access_key")

        return True

    def _generate_audio_file(self):
        """
        Generic method used as a Callback in TTSModule
            - must provided the audio file and write it on the disk

        .. raises:: FailToLoadSoundFile
        """

        polly = boto3.client('polly', 
                             aws_access_key_id=self.aws_access_key_id, 
                             aws_secret_access_key=self.aws_secret_access_key,
                             region_name= self.region_name)
        
        spoken_text = polly.synthesize_speech(Text=self.words,
                                              OutputFormat='mp3',
                                              VoiceId=self.voice)
                                              #TextType='ssml')

        FileManager.write_in_file(self.file_path, spoken_text['AudioStream'].read())


