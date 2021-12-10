# Generated by Django 3.2.7 on 2021-10-14 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('porteiros', '0002_auto_20211013_1517'),
        ('visitantes', '0005_auto_20211013_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitantes',
            name='cpf',
            field=models.CharField(blank=True, max_length=11, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='visitantes',
            name='data_nascimento',
            field=models.DateField(blank=True, verbose_name='Data de nascimento'),
        ),
        migrations.AlterField(
            model_name='visitantes',
            name='hoaraio_autorizacao',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Horário da autorização cadastral'),
        ),
        migrations.AlterField(
            model_name='visitantes',
            name='horario_chegada',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Horario do cadastro'),
        ),
        migrations.AlterField(
            model_name='visitantes',
            name='horario_saida',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Horário da finalização'),
        ),
        migrations.AlterField(
            model_name='visitantes',
            name='morador_responsavel',
            field=models.CharField(blank=True, max_length=194, verbose_name='Nome responsável por autorizar'),
        ),
        migrations.AlterField(
            model_name='visitantes',
            name='numero_casa',
            field=models.PositiveBigIntegerField(verbose_name='Numeração do cliente'),
        ),
        migrations.AlterField(
            model_name='visitantes',
            name='plava_veiculo',
            field=models.CharField(max_length=150, null=True, verbose_name='Email do cliente'),
        ),
        migrations.AlterField(
            model_name='visitantes',
            name='registrador_por',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='porteiros.porteiro', verbose_name='Administrador responsável pelo registro'),
        ),
    ]
