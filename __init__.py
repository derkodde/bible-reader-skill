from mycroft import MycroftSkill, intent_file_handler


class BibleReaderSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('skill.reader.bible.intent')
    def handle_skill_reader_bible(self, message):
        self.speak_dialog('skill.reader.bible')


def create_skill():
    return BibleReaderSkill()

