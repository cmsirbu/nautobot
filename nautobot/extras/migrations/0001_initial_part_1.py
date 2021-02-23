# Generated by Django 3.1.3 on 2021-02-20 08:07

from django.conf import settings
import django.contrib.postgres.fields
import django.core.serializers.json
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_cryptography.fields
import nautobot.extras.models.customfields
import nautobot.extras.models.relationships
import nautobot.extras.utils
import nautobot.utilities.fields
import nautobot.utilities.validators
import taggit.managers
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ConfigContext',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('owner_object_id', models.UUIDField(blank=True, default=None, null=True)),
                ('weight', models.PositiveSmallIntegerField(default=1000)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('is_active', models.BooleanField(default=True)),
                ('data', models.JSONField(encoder=django.core.serializers.json.DjangoJSONEncoder)),
            ],
            options={
                'ordering': ['weight', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('type', models.CharField(default='many-to-many', max_length=50)),
                ('source_label', models.CharField(blank=True, max_length=50)),
                ('source_hidden', models.BooleanField(default=False)),
                ('source_filter', models.JSONField(blank=True, null=True, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('destination_label', models.CharField(blank=True, max_length=50)),
                ('destination_hidden', models.BooleanField(default=False)),
                ('destination_filter', models.JSONField(blank=True, null=True, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('destination_type', models.ForeignKey(limit_choices_to=nautobot.extras.utils.FeatureQuery('relationships'), on_delete=django.db.models.deletion.CASCADE, related_name='destination_relationships', to='contenttypes.contenttype')),
                ('source_type', models.ForeignKey(limit_choices_to=nautobot.extras.utils.FeatureQuery('relationships'), on_delete=django.db.models.deletion.CASCADE, related_name='source_relationships', to='contenttypes.contenttype')),
            ],
            options={
                'ordering': ['name'],
            },
            managers=[
                ('objects', nautobot.extras.models.relationships.RelationshipManager()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('color', nautobot.utilities.fields.ColorField(default='9e9e9e', max_length=6)),
                ('description', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Webhook',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=150, unique=True)),
                ('type_create', models.BooleanField(default=False)),
                ('type_update', models.BooleanField(default=False)),
                ('type_delete', models.BooleanField(default=False)),
                ('payload_url', models.CharField(max_length=500)),
                ('enabled', models.BooleanField(default=True)),
                ('http_method', models.CharField(default='POST', max_length=30)),
                ('http_content_type', models.CharField(default='application/json', max_length=100)),
                ('additional_headers', models.TextField(blank=True)),
                ('body_template', models.TextField(blank=True)),
                ('secret', models.CharField(blank=True, max_length=255)),
                ('ssl_verification', models.BooleanField(default=True)),
                ('ca_file_path', models.CharField(blank=True, max_length=4096, null=True)),
                ('content_types', models.ManyToManyField(limit_choices_to=nautobot.extras.utils.FeatureQuery('webhooks'), related_name='webhooks', to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='TaggedItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('object_id', models.UUIDField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extras_taggeditem_tagged_items', to='contenttypes.contenttype')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extras_taggeditem_items', to='extras.tag')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('color', nautobot.utilities.fields.ColorField(default='9e9e9e', max_length=6)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('content_types', models.ManyToManyField(limit_choices_to=nautobot.extras.utils.FeatureQuery('statuses'), related_name='statuses', to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name_plural': 'statuses',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='RelationshipAssociation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('source_id', models.UUIDField()),
                ('destination_id', models.UUIDField()),
                ('destination_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='contenttypes.contenttype')),
                ('relationship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='associations', to='extras.relationship')),
                ('source_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='contenttypes.contenttype')),
            ],
        ),
        migrations.CreateModel(
            name='ObjectChange',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('time', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('user_name', models.CharField(editable=False, max_length=150)),
                ('request_id', models.UUIDField(editable=False)),
                ('action', models.CharField(max_length=50)),
                ('changed_object_id', models.UUIDField()),
                ('related_object_id', models.UUIDField(blank=True, null=True)),
                ('object_repr', models.CharField(editable=False, max_length=200)),
                ('object_data', models.JSONField(editable=False, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('changed_object_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='contenttypes.contenttype')),
                ('related_object_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='contenttypes.contenttype')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='changes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
        migrations.CreateModel(
            name='JobResult',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('completed', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(default='pending', max_length=30)),
                ('data', models.JSONField(blank=True, null=True, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('job_id', models.UUIDField(unique=True)),
                ('obj_type', models.ForeignKey(limit_choices_to=nautobot.extras.utils.FeatureQuery('job_results'), on_delete=django.db.models.deletion.CASCADE, related_name='job_results', to='contenttypes.contenttype')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='ImageAttachment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('object_id', models.UUIDField()),
                ('image', models.ImageField(height_field='image_height', upload_to=nautobot.extras.utils.image_upload, width_field='image_width')),
                ('image_height', models.PositiveSmallIntegerField()),
                ('image_width', models.PositiveSmallIntegerField()),
                ('name', models.CharField(blank=True, max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='GitRepository',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('remote_url', models.URLField(max_length=255, validators=[django.core.validators.URLValidator(schemes=['http', 'https'])])),
                ('branch', models.CharField(default='main', max_length=64)),
                ('current_head', models.CharField(blank=True, default='', max_length=48)),
                ('_token', django_cryptography.fields.encrypt(models.CharField(blank=True, default='', max_length=200))),
                ('username', models.CharField(blank=True, default='', max_length=64)),
                ('provided_contents', models.JSONField(blank=True, default=list, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'verbose_name': 'Git repository',
                'verbose_name_plural': 'Git repositories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ExportTemplate',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('owner_object_id', models.UUIDField(blank=True, default=None, null=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('template_code', models.TextField()),
                ('mime_type', models.CharField(blank=True, max_length=50)),
                ('file_extension', models.CharField(blank=True, max_length=15)),
                ('content_type', models.ForeignKey(limit_choices_to=nautobot.extras.utils.FeatureQuery('export_templates'), on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('owner_content_type', models.ForeignKey(blank=True, default=None, limit_choices_to=nautobot.extras.utils.FeatureQuery('export_template_owners'), null=True, on_delete=django.db.models.deletion.CASCADE, related_name='export_template_owners', to='contenttypes.contenttype')),
            ],
            options={
                'ordering': ['content_type', 'name'],
            },
        ),
        migrations.CreateModel(
            name='CustomLink',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('text', models.CharField(max_length=500)),
                ('target_url', models.CharField(max_length=500)),
                ('weight', models.PositiveSmallIntegerField(default=100)),
                ('group_name', models.CharField(blank=True, max_length=50)),
                ('button_class', models.CharField(default='default', max_length=30)),
                ('new_window', models.BooleanField()),
                ('content_type', models.ForeignKey(limit_choices_to=nautobot.extras.utils.FeatureQuery('custom_links'), on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'ordering': ['group_name', 'weight', 'name'],
            },
        ),
        migrations.CreateModel(
            name='CustomField',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('type', models.CharField(default='text', max_length=50)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('label', models.CharField(blank=True, max_length=50)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('required', models.BooleanField(default=False)),
                ('filter_logic', models.CharField(default='loose', max_length=50)),
                ('default', models.JSONField(blank=True, null=True, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('weight', models.PositiveSmallIntegerField(default=100)),
                ('validation_minimum', models.PositiveIntegerField(blank=True, null=True)),
                ('validation_maximum', models.PositiveIntegerField(blank=True, null=True)),
                ('validation_regex', models.CharField(blank=True, max_length=500, validators=[nautobot.utilities.validators.validate_regex])),
                ('choices', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, null=True, size=None)),
                ('content_types', models.ManyToManyField(limit_choices_to=nautobot.extras.utils.FeatureQuery('custom_fields'), related_name='custom_fields', to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ['weight', 'name'],
            },
            managers=[
                ('objects', nautobot.extras.models.customfields.CustomFieldManager()),
            ],
        ),
    ]
