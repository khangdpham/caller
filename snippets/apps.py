from django.apps import AppConfig


class SnippetsConfig(AppConfig):
    name = 'snippets'
    def ready(self):
      from snippets.scheduleUpdater import updater
      try:
        updater.start()
        print("Starting APPP")
      except Exception as e:
        print(str(e))
~                       
