from django.core.management.base import BaseCommand
import polib
from googletrans import Translator
import os
from django.conf import settings

class Command(BaseCommand):
    help = 'Automatically translates the Arabic django.po file using Google Translate'

    def handle(self, *args, **options):
        # Path to the Arabic django.po file
        po_file_path = os.path.join(settings.BASE_DIR, 'locale', 'ar', 'LC_MESSAGES', 'django.po')
        
        if not os.path.exists(po_file_path):
            self.stdout.write(self.style.ERROR('django.po file not found. Run "python manage.py makemessages -l ar" first.'))
            return
        
        # Load the .po file
        po = polib.pofile(po_file_path)
        translator = Translator()

        # Counter for translated entries
        translated_count = 0

        # Iterate through each entry in the .po file
        for entry in po:
            # Only translate if the msgstr is empty
            if not entry.msgstr and entry.msgid:
                try:
                    # Translate msgid from English to Arabic
                    translation = translator.translate(entry.msgid, src='en', dest='ar')
                    entry.msgstr = translation.text
                    translated_count += 1
                    self.stdout.write(self.style.SUCCESS(f'Translated: "{entry.msgid}" -> "{entry.msgstr}"'))
                except Exception as e:
                    self.stdout.write(self.style.WARNING(f'Failed to translate "{entry.msgid}": {str(e)}'))

        # Save the updated .po file
        po.save()
        self.stdout.write(self.style.SUCCESS(f'Successfully translated {translated_count} entries in {po_file_path}'))

        # Compile the .mo file
        po.save_as_mofile(os.path.splitext(po_file_path)[0] + '.mo')
        self.stdout.write(self.style.SUCCESS('Compiled .mo file'))