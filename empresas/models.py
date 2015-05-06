# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser, User
from cloudinary.models import CloudinaryField
from django.db.models import signals

#Campos Varchar
#Pequenos : 50
#Medios   : 150
#Grandes  : 250

class Empresa(models.Model):
    logo = models.CharField(default='semfoto.png', max_length=100, blank=True, null=True)
    razao_social = models.CharField(db_index=True,max_length=150, blank=False)
    nome_fantasia = models.CharField(db_index=True,max_length=150, blank=True)
    cnpj = models.CharField(max_length=50, blank=True, null=True)
    num_registro = models.CharField(max_length=150, blank=True)
    endereco_rua = models.CharField(max_length=250, blank=True, null=True)
    endereco_numero = models.CharField(max_length=250, blank=True, null=True)
    endereco_complemento = models.CharField(max_length=250, blank=True, null=True)
    endereco_bairro = models.CharField(max_length=250, blank=True, null=True)
    endereco_cidade = models.CharField(max_length=250, blank=True, null=True)
    endereco_estado = models.CharField(max_length=250, blank=True, null=True)
    endereco_pais = models.CharField(max_length=250, blank=True, null=True)
    endereco_cep = models.CharField(max_length=250, blank=True, null=True)
    telefone_contato = models.CharField(max_length=50, blank=True, null=True)
    telefone_financeiro = models.CharField(max_length=50, blank=True, null=True)
    email_contato = models.CharField(max_length=150, blank=False)
    email_financeiro = models.CharField(max_length=150, blank=True, null=True)
    facebook = models.CharField(max_length=150, blank=True, null=True)
    googleplus = models.CharField(max_length=150, blank=True, null=True)
    twitter = models.CharField(max_length=150, blank=True, null=True)
    skype = models.CharField(max_length=150, blank=True, null=True)
    conta_banco = models.CharField(max_length=50, blank=True, null=True)
    conta_agencia = models.CharField(max_length=50, blank=True, null=True)
    conta_corrente = models.CharField(max_length=50, blank=True, null=True)
    conta_carteira = models.CharField(max_length=50, blank=True, null=True)
    conta_codigo_cedente = models.CharField(max_length=50, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now=False, auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True, auto_now_add=True)
    tags = models.CharField(max_length=250, blank=True, null=True)
    ativo = models.CharField(default="SIM", max_length=50, blank=False)

def empresa_formatacao(signal, instance, sender, **kwargs):
    if instance.razao_social:
        instance.razao_social = instance.razao_social.title().strip()
    if instance.nome_fantasia:
        instance.nome_fantasia = instance.nome_fantasia.upper().strip()
    if instance.email_contato:
        instance.email_contato = instance.email_contato.lower().strip()
    if instance.email_financeiro:
        instance.email_financeiro = instance.email_financeiro.lower().strip()

signals.pre_save.connect(empresa_formatacao, sender=Empresa)

    

class Usuario(AbstractUser):
    # username
    # first_name
    # last_name
    # email
    # password
    # is_staff
    # is_active
    # is_superuser
    # last_login
    # date_joined
    cpf = models.CharField(_(u'CPF'), max_length=50, blank=True, null=True)
    rg = models.CharField(_(u'RG'), max_length=50, blank=True, null=True)
    facebook = models.CharField(_(u'Facebook'), max_length=150, blank=True, null=True)
    googleplus = models.CharField(_(u'Google Plus'), max_length=150, blank=True, null=True)
    twitter = models.CharField(_(u'Twitter'), max_length=150, blank=True, null=True)
    skype = models.CharField(_(u'Skype'), max_length=150, blank=True, null=True)
    telefone_fixo = models.CharField(_(u'Telefone Fixo'), max_length=50, blank=True, null=True)
    telefone_celular = models.CharField(_(u'Telefone Celular'), max_length=50, blank=True, null=True)
    foto = CloudinaryField(_(u'foto'), blank=True, null=True)
    idioma = models.CharField(_(u'Idioma'), max_length=50, blank=True)
    empresa = models.ForeignKey(Empresa, related_name="usuario_empresa_id", blank=True, null=True)

    class Meta:
        verbose_name = _(u'Usuário')
        verbose_name_plural = _(u'Usuários')
        ordering = ['first_name']

    def __unicode__(self):
        return u'{username} ({email})'.format(username=self.username, email=self.email)

def usuario_formatacao(signal, instance, sender, **kwargs):
    if instance.first_name:
        instance.first_name = instance.first_name.title().strip()
    if instance.last_name:
        instance.last_name = instance.last_name.title().strip()
    if instance.email:
        instance.email = instance.email.lower().strip()
    if instance.password:
        instance.password = instance.password.strip()

    instance.is_staff = False
    instance.is_superuser = False

signals.pre_save.connect(usuario_formatacao, sender=Usuario)

class Sistema(models.Model):
    tipo = models.CharField(max_length=50, blank=True, null=True)
    nome = models.CharField(max_length=150, blank=True, null=True)
    empresa = models.ForeignKey(Empresa, related_name="sistema_empresa_id", blank=True, null=True)
    tags = models.CharField(max_length=250, blank=True, null=True)
    descricao = models.CharField(max_length=250, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now=False, auto_now_add=True)
    ativo = models.CharField(default="SIM", max_length=50, blank=False)

    def __unicode__(self):
        return u'{nome}'.format(nome=self.nome)

def sistema_formatacao(signal, instance, sender, **kwargs):
    if instance.tipo:
        instance.tipo = instance.tipo.upper().strip()
    if instance.nome:
        instance.nome = instance.nome.upper().strip()
    if instance.tags:
        instance.tags = instance.tags.upper().strip()

signals.pre_save.connect(sistema_formatacao, sender=Sistema)


class Pessoa(models.Model):
    tipo = models.ForeignKey(Sistema, related_name="pessoa_tipo_id", blank=True, null=True)
    nome = models.CharField(db_index=True,max_length=150, blank=True)
    cpf = models.CharField(max_length=50, blank=True, null=True)
    rg = models.CharField(max_length=50, blank=True, null=True)
    conta_banco = models.CharField(max_length=50, blank=True, null=True)
    conta_corrente = models.CharField(max_length=50, blank=True, null=True)
    conta_agencia = models.CharField(max_length=50, blank=True, null=True)
    endereco_rua = models.CharField(max_length=250, blank=True, null=True)
    endereco_numero = models.CharField(max_length=50, blank=True, null=True)
    endereco_complemento = models.CharField(max_length=250, blank=True, null=True)
    endereco_bairro = models.CharField(max_length=250, blank=True, null=True)
    endereco_cidade = models.CharField(max_length=250, blank=True, null=True)
    endereco_estado = models.CharField(max_length=250, blank=True, null=True)
    endereco_pais = models.CharField(max_length=250, blank=True, null=True)
    endereco_cep = models.CharField(max_length=50, blank=True, null=True)
    telefone_fixo = models.CharField(max_length=50, blank=True, null=True)
    telefone_celular = models.CharField(max_length=50, blank=True, null=True)
    email_pessoal = models.CharField(max_length=250, blank=True, null=True)
    email_empresarial = models.CharField(max_length=250, blank=True, null=True)
    facebook = models.CharField(db_index=True,max_length=150, blank=True)
    googleplus = models.CharField(db_index=True,max_length=150, blank=True)
    skype = models.CharField(db_index=True,max_length=150, blank=True)
    twitter = models.CharField(db_index=True,max_length=150, blank=True)
    empresa = models.ForeignKey(Empresa,related_name="pessoa_empresa_id")
    usuario = models.ForeignKey(Usuario,related_name="pessoa_usuario_id")
    data_cadastro = models.DateTimeField(auto_now=False, auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True, auto_now_add=True)
    ativo = models.CharField(default="SIM", max_length=50, blank=False)
    anotacacoes = models.CharField(max_length=250, blank=True, null=True)
    grupo_pessoa = models.CharField(db_index=True,max_length=150, blank=True)
    tags = models.CharField(max_length=250, blank=True, null=True)

    def __unicode__(self):
        return u'{nome} ({email_pessoal})'.format(nome=self.nome, email_pessoal=self.email_pessoal)

def pessoa_formatacao(signal, instance, sender, **kwargs):
    instance.nome = instance.nome.title().strip()
    instance.endereco_rua = instance.endereco_rua.title().strip()

signals.pre_save.connect(pessoa_formatacao, sender=Pessoa)
