# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'CadastroFieis.fotoFiel'
        db.delete_column(u'cadastro_fieis_cadastrofieis', 'fotoFiel')

        # Adding field 'CadastroFieis.foto'
        db.add_column('cadastro_fieis_cadastrofieis', 'foto',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'CadastroFieis.fotoFiel'
        db.add_column(u'cadastro_fieis_cadastrofieis', 'fotoFiel',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'CadastroFieis.foto'
        db.delete_column('cadastro_fieis_cadastrofieis', 'foto')


    models = {
        u'cadastro_fieis.cadastrofieis': {
            'Meta': {'ordering': "['criado_em']", 'object_name': 'CadastroFieis'},
            'area1PTS': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'area2PTS': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'area3PTS': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'area4PTS': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'bairro': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cargosefuncoesDE': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'cep': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'cidade': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'classeEBDDE': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'congregacaoDE': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'conjuge': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'cpf': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '11'}),
            'crente': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'criado_em': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dataBatismoDE': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'dataCasamento': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'dataConversaoDE': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'dataNascimento': ('django.db.models.fields.DateField', [], {'max_length': '12'}),
            'dataSaida': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '100'}),
            'endereco': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'estadoCivil': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'funcao1PTS': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'funcao2PTS': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'funcao3PTS': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'funcao4PTS': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'igrejaDBatismoDE': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'igrejaDE': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'igrejaOrigemDE': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'naturalDe': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nomeMae': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'nomePai': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'orgpertenceDE': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'recebidoCartaDataDE': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'rg': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'telefone': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'tituloEleitor': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'uf': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['cadastro_fieis']