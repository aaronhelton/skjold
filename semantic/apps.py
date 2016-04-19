from django.apps import AppConfig


class SemanticConfig(AppConfig):
  name = 'semantic'
  verbose_name = 'SkjoLD Semantic Application'

  def ready(self):
    import semantic.signals
