# Generated by Django 5.1.2 on 2024-10-30 20:38

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=100, unique=True)),
                ('tipo_clientes', models.CharField(choices=[('P', 'Particular'), ('E', 'Empresa')], max_length=2)),
                ('direccion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MetodoPago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metodo_pago', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('tipo_pago', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_ultima_actualizacion', models.DateTimeField(auto_now=True)),
                ('pagado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PiezaMotor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pieza', models.CharField(max_length=100)),
                ('nombre', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descripción', models.TextField()),
                ('stock_disponible', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proveedor', models.CharField(max_length=100)),
                ('nombre_proveedor', models.CharField(max_length=100)),
                ('telefono', models.TextField()),
                ('correo', models.CharField(max_length=100, unique=True)),
                ('direccion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empleado', models.CharField(max_length=100)),
                ('nombre', models.TextField()),
                ('apellido', models.TextField()),
                ('cargo', models.CharField(max_length=100)),
                ('fecha_contratacion', models.DateField(blank=True, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EmpresaVentaPiezasCoche.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pedido', models.CharField(max_length=100)),
                ('fecha_pedido', models.DateField()),
                ('total_importe', models.IntegerField()),
                ('estado', models.CharField(choices=[('P', 'Pendiente'), ('ENV', 'Enviado'), ('ENTR', 'Entregado')], max_length=4)),
                ('cliente_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedido_cliente', to='EmpresaVentaPiezasCoche.cliente')),
                ('metodo_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EmpresaVentaPiezasCoche.metodopago')),
            ],
        ),
        migrations.CreateModel(
            name='PiezaMotor_Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('precioTotal', models.FloatField(default=0.0)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EmpresaVentaPiezasCoche.pedido')),
                ('pieza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EmpresaVentaPiezasCoche.piezamotor')),
            ],
        ),
        migrations.AddField(
            model_name='piezamotor',
            name='pedido',
            field=models.ManyToManyField(through='EmpresaVentaPiezasCoche.PiezaMotor_Pedido', to='EmpresaVentaPiezasCoche.pedido'),
        ),
        migrations.AddField(
            model_name='piezamotor',
            name='proveedor',
            field=models.ManyToManyField(to='EmpresaVentaPiezasCoche.proveedor'),
        ),
    ]
