from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("tasks", "0080_channel_repository_configuration")]

    operations = [
        migrations.AddField(
            model_name="loop",
            name="client_provenance",
            field=models.CharField(
                blank=True,
                choices=[("posthog_desktop", "PostHog Desktop")],
                editable=False,
                max_length=32,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="sandboxsession",
            name="client_provenance",
            field=models.CharField(
                blank=True,
                choices=[("posthog_desktop", "PostHog Desktop")],
                editable=False,
                max_length=32,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="task",
            name="client_provenance",
            field=models.CharField(
                blank=True,
                choices=[("posthog_desktop", "PostHog Desktop")],
                editable=False,
                max_length=32,
                null=True,
            ),
        ),
    ]
