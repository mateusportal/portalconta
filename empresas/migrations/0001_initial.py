# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Empresa'
        db.create_table(u'empresas_empresa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('logo', self.gf('django.db.models.fields.CharField')(default='semfoto.png', max_length=100, null=True, blank=True)),
            ('razao_social', self.gf('django.db.models.fields.CharField')(max_length=150, db_index=True)),
            ('nome_fantasia', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=150, blank=True)),
            ('cnpj', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('num_registro', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('endereco_rua', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('endereco_numero', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('endereco_complemento', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('endereco_bairro', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('endereco_cidade', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('endereco_estado', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('endereco_pais', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('endereco_cep', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('telefone_contato', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('telefone_financeiro', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('email_contato', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('email_financeiro', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('facebook', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('googleplus', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('conta_banco', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('conta_agencia', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('conta_corrente', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('conta_carteira', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('conta_codigo_cedente', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('data_cadastro', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('data_alteracao', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('tags', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('ativo', self.gf('django.db.models.fields.CharField')(default='SIM', max_length=50)),
        ))
        db.send_create_signal(u'empresas', ['Empresa'])

        # Adding model 'Usuario'
        db.create_table(u'empresas_usuario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('cpf', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('rg', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('facebook', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('googleplus', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('telefone_fixo', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('telefone_celular', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('foto', self.gf('cloudinary.models.CloudinaryField')(max_length=100, null=True, blank=True)),
            ('idioma', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='usuario_empresa_id', null=True, to=orm['empresas.Empresa'])),
        ))
        db.send_create_signal(u'empresas', ['Usuario'])

        # Adding M2M table for field groups on 'Usuario'
        m2m_table_name = db.shorten_name(u'empresas_usuario_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('usuario', models.ForeignKey(orm[u'empresas.usuario'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['usuario_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'Usuario'
        m2m_table_name = db.shorten_name(u'empresas_usuario_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('usuario', models.ForeignKey(orm[u'empresas.usuario'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['usuario_id', 'permission_id'])

        # Adding model 'Sistema'
        db.create_table(u'empresas_sistema', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='sistema_empresa_id', null=True, to=orm['empresas.Empresa'])),
            ('tags', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('data_cadastro', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('ativo', self.gf('django.db.models.fields.CharField')(default='SIM', max_length=50)),
        ))
        db.send_create_signal(u'empresas', ['Sistema'])

        # Adding model 'Pessoa'
        db.create_table(u'empresas_pessoa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='pessoa_tipo_id', null=True, to=orm['empresas.Sistema'])),
            ('nome', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=150, blank=True)),
            ('cpf', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('rg', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('conta_banco', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('conta_corrente', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('conta_agencia', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('endereco_rua', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('endereco_numero', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('endereco_complemento', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('endereco_bairro', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('endereco_cidade', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('endereco_estado', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('endereco_pais', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('endereco_cep', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('telefone_fixo', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('telefone_celular', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('email_pessoal', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('email_empresarial', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('facebook', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=150, blank=True)),
            ('googleplus', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=150, blank=True)),
            ('skype', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=150, blank=True)),
            ('twitter', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=150, blank=True)),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(related_name='pessoa_empresa_id', to=orm['empresas.Empresa'])),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(related_name='pessoa_usuario_id', to=orm['empresas.Usuario'])),
            ('data_cadastro', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('data_alteracao', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('ativo', self.gf('django.db.models.fields.CharField')(default='SIM', max_length=50)),
            ('anotacacoes', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('grupo_pessoa', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=150, blank=True)),
            ('tags', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
        ))
        db.send_create_signal(u'empresas', ['Pessoa'])


    def backwards(self, orm):
        # Deleting model 'Empresa'
        db.delete_table(u'empresas_empresa')

        # Deleting model 'Usuario'
        db.delete_table(u'empresas_usuario')

        # Removing M2M table for field groups on 'Usuario'
        db.delete_table(db.shorten_name(u'empresas_usuario_groups'))

        # Removing M2M table for field user_permissions on 'Usuario'
        db.delete_table(db.shorten_name(u'empresas_usuario_user_permissions'))

        # Deleting model 'Sistema'
        db.delete_table(u'empresas_sistema')

        # Deleting model 'Pessoa'
        db.delete_table(u'empresas_pessoa')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'empresas.empresa': {
            'Meta': {'object_name': 'Empresa'},
            'ativo': ('django.db.models.fields.CharField', [], {'default': "'SIM'", 'max_length': '50'}),
            'cnpj': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'conta_agencia': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'conta_banco': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'conta_carteira': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'conta_codigo_cedente': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'conta_corrente': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'data_alteracao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'data_cadastro': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email_contato': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'email_financeiro': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'endereco_bairro': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'endereco_cep': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'endereco_cidade': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'endereco_complemento': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'endereco_estado': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'endereco_numero': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'endereco_pais': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'endereco_rua': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'googleplus': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.CharField', [], {'default': "'semfoto.png'", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nome_fantasia': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '150', 'blank': 'True'}),
            'num_registro': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'razao_social': ('django.db.models.fields.CharField', [], {'max_length': '150', 'db_index': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'telefone_contato': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'telefone_financeiro': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'})
        },
        u'empresas.pessoa': {
            'Meta': {'object_name': 'Pessoa'},
            'anotacacoes': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'ativo': ('django.db.models.fields.CharField', [], {'default': "'SIM'", 'max_length': '50'}),
            'conta_agencia': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'conta_banco': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'conta_corrente': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'cpf': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'data_alteracao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'data_cadastro': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email_empresarial': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'email_pessoal': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pessoa_empresa_id'", 'to': u"orm['empresas.Empresa']"}),
            'endereco_bairro': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'endereco_cep': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'endereco_cidade': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'endereco_complemento': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'endereco_estado': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'endereco_numero': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'endereco_pais': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'endereco_rua': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '150', 'blank': 'True'}),
            'googleplus': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '150', 'blank': 'True'}),
            'grupo_pessoa': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '150', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '150', 'blank': 'True'}),
            'rg': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '150', 'blank': 'True'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'telefone_celular': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'telefone_fixo': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'pessoa_tipo_id'", 'null': 'True', 'to': u"orm['empresas.Sistema']"}),
            'twitter': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '150', 'blank': 'True'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pessoa_usuario_id'", 'to': u"orm['empresas.Usuario']"})
        },
        u'empresas.sistema': {
            'Meta': {'object_name': 'Sistema'},
            'ativo': ('django.db.models.fields.CharField', [], {'default': "'SIM'", 'max_length': '50'}),
            'data_cadastro': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'sistema_empresa_id'", 'null': 'True', 'to': u"orm['empresas.Empresa']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'empresas.usuario': {
            'Meta': {'ordering': "['first_name']", 'object_name': 'Usuario'},
            'cpf': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'usuario_empresa_id'", 'null': 'True', 'to': u"orm['empresas.Empresa']"}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'foto': ('cloudinary.models.CloudinaryField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'googleplus': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idioma': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'rg': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'telefone_celular': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'telefone_fixo': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['empresas']