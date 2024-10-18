# Generated by Django 5.1.2 on 2024-10-18 21:22

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
                ('id_cliente', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=100, unique=True)),
                ('tipo_Clientes', models.CharField(choices=[('P', 'Particular'), ('E', 'Empresa')], max_length=2)),
                ('direccion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_empresa', models.CharField(max_length=100)),
                ('nombre', models.TextField()),
                ('telefono', models.TextField()),
                ('direccion', models.TextField()),
                ('email_contacto', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MetodoPago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_metodo_pago', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('tipo_pago', models.CharField(max_length=100)),
                ('fecha_Creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_Ultima_Actualizacion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PiezaMotor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_pieza', models.CharField(max_length=100)),
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
                ('id_proveedor', models.CharField(max_length=100)),
                ('nombre_proveedor', models.CharField(max_length=100)),
                ('telefono', models.TextField()),
                ('correo', models.CharField(max_length=100, unique=True)),
                ('direccion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_Provincia', models.CharField(max_length=100)),
                ('nombre', models.TextField()),
                ('comunidad', models.CharField(max_length=100)),
                ('num_habitantes', models.IntegerField()),
                ('codigo_postal', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_empleado', models.CharField(max_length=100)),
                ('nombre', models.TextField()),
                ('apellido', models.TextField()),
                ('cargo', models.CharField(max_length=100)),
                ('fecha_contratacion', models.DateField(blank=True, null=True)),
                ('id_empresa_empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EmpresaVentaPiezasCoche.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_pedido', models.CharField(max_length=100)),
                ('fecha_pedido', models.DateField()),
                ('total_importe', models.IntegerField()),
                ('estado', models.CharField(choices=[('P', 'Pendiente'), ('ENV', 'Enviado'), ('ENTR', 'Entregado')], max_length=4)),
                ('id_cliente_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EmpresaVentaPiezasCoche.cliente')),
                ('id_metodo_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EmpresaVentaPiezasCoche.metodopago')),
            ],
        ),
        migrations.CreateModel(
            name='PiezaMotor_Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('precioTotal', models.FloatField(default=0.0)),
                ('id_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EmpresaVentaPiezasCoche.pedido')),
                ('id_pieza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EmpresaVentaPiezasCoche.piezamotor')),
            ],
        ),
        migrations.AddField(
            model_name='piezamotor',
            name='id_pedido',
            field=models.ManyToManyField(through='EmpresaVentaPiezasCoche.PiezaMotor_Pedido', to='EmpresaVentaPiezasCoche.pedido'),
        ),
        migrations.AddField(
            model_name='piezamotor',
            name='proveedor',
            field=models.ManyToManyField(to='EmpresaVentaPiezasCoche.proveedor'),
        ),
        migrations.CreateModel(
            name='DireccionPrincipal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_direccion', models.CharField(max_length=100)),
                ('calle', models.TextField()),
                ('provincia', models.CharField(max_length=100)),
                ('codigo_postal', models.IntegerField()),
                ('numero', models.CharField(blank=True, max_length=10, null=True)),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EmpresaVentaPiezasCoche.cliente')),
                ('id_Empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EmpresaVentaPiezasCoche.empresa')),
                ('id_Provincia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EmpresaVentaPiezasCoche.provincia')),
            ],
        ),
    ]
