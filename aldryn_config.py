from aldryn_client import forms


class Form(forms.BaseForm):
    def to_settings(self, data, settings):
        from functools import partial
        from aldryn_addons.utils import djsenv
        import yurl

        env = partial(djsenv, settings=settings)

        custom_media_domain = env("CUSTOM_MEDIA_DOMAIN")

        if custom_media_domain and "AWS_MEDIA_BUCKET_PREFIX" in settings:
            settings.update(
                {
                    "AWS_MEDIA_DOMAIN": custom_media_domain,
                    "MEDIA_URL": yurl.URL(
                        scheme="https",
                        host=custom_media_domain,
                        path=settings["AWS_MEDIA_BUCKET_PREFIX"],
                    ).as_string(),
                }
            )

        return settings
