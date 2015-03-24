# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Sistema'
        db.create_table(u'contas_sistema', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sistema_empresa_id', to=orm['empresas.Empresa'])),
            ('tags', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('data_cadastro', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('ativo', self.gf('django.db.models.fields.CharField')(default='SIM', max_length=50)),
        ))
        db.send_create_signal(u'contas', ['Sistema'])

        # Adding model 'Caixa'
        db.create_table(u'contas_caixa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pessoa', self.gf('django.db.models.fields.related.ForeignKey')(related_name='caixa_pessoa_id', to=orm['empresas.Pessoa'])),
            ('valor_bruto', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=2)),
            ('data_vencimento', self.gf('django.db.models.fields.DateTimeField')()),
            ('data_pagamento', self.gf('django.db.models.fields.DateTimeField')()),
            ('valor_multa', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=2)),
            ('valor_juros', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=2)),
            ('valor_desconto', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=2)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('operacao', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('data_cadastro', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('data_alteracao', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('ativo', self.gf('django.db.models.fields.CharField')(default='SIM', max_length=50)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(related_name='caixa_usuario_id', to=orm['empresas.Pessoa'])),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(related_name='caixa_empresa_id', to=orm['empresas.Empresa'])),
            ('observacao', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('tags', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('data_boleto', self.gf('django.db.models.fields.DateTimeField')()),
            ('processo', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('categoria', self.gf('django.db.models.fields.related.ForeignKey')(related_name='caixa_categoria_id', to=orm['contas.Sistema'])),
            ('grupo_id', self.gf('django.db.models.fields.related.ForeignKey')(related_name='caixa_grupo_id', to=orm['contas.Sistema'])),
            ('subgrupo', self.gf('django.db.models.fields.related.ForeignKey')(related_name='caixa_subgrupo_id', to=orm['contas.Sistema'])),
        ))
        db.send_create_signal(u'contas', ['Caixa'])

        # Adding model 'Vinculo'
        db.create_table(u'contas_vinculo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('caixa_pai', self.gf('django.db.models.fields.related.ForeignKey')(related_name='vinculo_caixa_pai_id', to=orm['contas.Caixa'])),
            ('caixa_filho', self.gf('django.db.models.fields.related.ForeignKey')(related_name='vinculo_caixa_filho_id', to=orm['contas.Caixa'])),
            ('observacao', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('rastreador', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('tags', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(related_name='vinculo_empresa_id', to=orm['empresas.Empresa'])),
        ))
        db.send_create_signal(u'contas', ['Vinculo'])

        # Adding model 'Cheque'
        db.create_table(u'contas_cheque', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('banco', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('agencia', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('numero_cheque', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('valor', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=2)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('data_recebido', self.gf('django.db.models.fields.DateTimeField')()),
            ('data_compensar', self.gf('django.db.models.fields.DateTimeField')()),
            ('data_compensado', self.gf('django.db.models.fields.DateTimeField')()),
            ('caixa', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cheque_caixa_id', to=orm['contas.Caixa'])),
        ))
        db.send_create_signal(u'contas', ['Cheque'])


    def backwards(self, orm):
        # Deleting model 'Sistema'
        db.delete_table(u'contas_sistema')

        # Deleting model 'Caixa'
        db.delete_table(u'contas_caixa')

        # Deleting model 'Vinculo'
        db.delete_table(u'contas_vinculo')

        # Deleting model 'Cheque'
        db.delete_table(u'contas_cheque')


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
        u'contas.caixa': {
            'Meta': {'object_name': 'Caixa'},
            'ativo': ('django.db.models.fields.CharField', [], {'default': "'SIM'", 'max_length': '50'}),
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'caixa_categoria_id'", 'to': u"orm['contas.Sistema']"}),
            'data_alteracao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'data_boleto': ('django.db.models.fields.DateTimeField', [], {}),
            'data_cadastro': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data_pagamento': ('django.db.models.fields.DateTimeField', [], {}),
            'data_vencimento': ('django.db.models.fields.DateTimeField', [], {}),
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'caixa_empresa_id'", 'to': u"orm['empresas.Empresa']"}),
            'grupo_id': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'caixa_grupo_id'", 'to': u"orm['contas.Sistema']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observacao': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'operacao': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'caixa_pessoa_id'", 'to': u"orm['empresas.Pessoa']"}),
            'processo': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'subgrupo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'caixa_subgrupo_id'", 'to': u"orm['contas.Sistema']"}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'caixa_usuario_id'", 'to': u"orm['empresas.Pessoa']"}),
            'valor_bruto': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2'}),
            'valor_desconto': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2'}),
            'valor_juros': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2'}),
            'valor_multa': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2'})
        },
        u'contas.cheque': {
            'Meta': {'object_name': 'Cheque'},
            'agencia': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'banco': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'caixa': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cheque_caixa_id'", 'to': u"orm['contas.Caixa']"}),
            'data_compensado': ('django.db.models.fields.DateTimeField', [], {}),
            'data_compensar': ('django.db.models.fields.DateTimeField', [], {}),
            'data_recebido': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'numero_cheque': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'valor': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2'})
        },
        u'contas.sistema': {
            'Meta': {'object_name': 'Sistema'},
            'ativo': ('django.db.models.fields.CharField', [], {'default': "'SIM'", 'max_length': '50'}),
            'data_cadastro': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sistema_empresa_id'", 'to': u"orm['empresas.Empresa']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'contas.vinculo': {
            'Meta': {'object_name': 'Vinculo'},
            'caixa_filho': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'vinculo_caixa_filho_id'", 'to': u"orm['contas.Caixa']"}),
            'caixa_pai': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'vinculo_caixa_pai_id'", 'to': u"orm['contas.Caixa']"}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'vinculo_empresa_id'", 'to': u"orm['empresas.Empresa']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observacao': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'rastreador': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'})
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
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '150', 'blank': 'True'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pessoa_usuario_id'", 'to': u"orm['empresas.Usuario']"})
        },
        u'empresas.usuario': {
            'Meta': {'ordering': "['first_name']", 'object_name': 'Usuario'},
            'cpf': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'usuario_empresa_id'", 'null': 'True', 'to': u"orm['empresas.Empresa']"}),
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

    complete_apps = ['contas']