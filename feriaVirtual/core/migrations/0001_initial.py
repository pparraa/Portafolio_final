# Generated by Django 3.1.1 on 2020-10-18 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calidad',
            fields=[
                ('id_calidad', models.BooleanField(primary_key=True, serialize=False)),
                ('detalle', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'calidad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id_calificacion', models.IntegerField(primary_key=True, serialize=False)),
                ('des_calificacion', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'calificacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id_comuna', models.IntegerField(primary_key=True, serialize=False)),
                ('des_comuna', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'comuna',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id_contrato', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_inicio', models.DateField()),
                ('fecha_termino', models.DateField()),
                ('vigencia', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'contrato',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Costos',
            fields=[
                ('id_costo', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=30)),
                ('valor', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'costos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetalleLocal',
            fields=[
                ('id_detalle_local', models.IntegerField(primary_key=True, serialize=False)),
                ('precio', models.IntegerField()),
                ('kilo', models.IntegerField()),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'detalle_local',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetalleOferta',
            fields=[
                ('id_detalle_of', models.IntegerField(primary_key=True, serialize=False)),
                ('kilo', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('fecha_cosecha', models.DateField()),
                ('id_publicacion', models.IntegerField()),
            ],
            options={
                'db_table': 'detalle_oferta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetalleSolicitud',
            fields=[
                ('id_pedido', models.IntegerField(primary_key=True, serialize=False)),
                ('kilos', models.DecimalField(decimal_places=4, max_digits=14)),
            ],
            options={
                'db_table': 'detalle_solicitud',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id_empresa', models.IntegerField(primary_key=True, serialize=False)),
                ('rut_empresa', models.CharField(max_length=9)),
                ('razon_social', models.CharField(max_length=50)),
                ('giro_empresa', models.CharField(max_length=150)),
                ('direccion_empresa', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'empresa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Especie',
            fields=[
                ('id_especie', models.IntegerField(primary_key=True, serialize=False)),
                ('des_especie', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'especie',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EstadoContrato',
            fields=[
                ('id_estado', models.IntegerField(primary_key=True, serialize=False)),
                ('des_estado', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'estado_contrato',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EstadoEmpresa',
            fields=[
                ('id_estado', models.IntegerField(primary_key=True, serialize=False)),
                ('des_estado', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'estado_empresa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EstadoPedido',
            fields=[
                ('id_estado', models.IntegerField(primary_key=True, serialize=False)),
                ('desc_estado', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'estado_pedido',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EstadoSolicitud',
            fields=[
                ('id_estado', models.IntegerField(primary_key=True, serialize=False)),
                ('des_estado', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'estado_solicitud',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EstadoUsuario',
            fields=[
                ('id_estado', models.IntegerField(primary_key=True, serialize=False)),
                ('des_estado', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'estado_usuario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EstadoVenta',
            fields=[
                ('id_estado', models.IntegerField(primary_key=True, serialize=False)),
                ('des_estado', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'estado_venta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id_imagen', models.IntegerField(primary_key=True, serialize=False)),
                ('desc_imagen', models.CharField(max_length=100)),
                ('ext_imagen', models.CharField(max_length=6)),
                ('imagen', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'db_table': 'imagen',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OfertaProductor',
            fields=[
                ('id_oferta', models.IntegerField(primary_key=True, serialize=False)),
                ('id_orden', models.IntegerField()),
            ],
            options={
                'db_table': 'oferta_productor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrdenCompra',
            fields=[
                ('id_orden', models.IntegerField(primary_key=True, serialize=False)),
                ('total', models.IntegerField()),
            ],
            options={
                'db_table': 'orden_compra',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id_pago', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=30)),
                ('monto', models.IntegerField(blank=True, null=True)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('kilos', models.FloatField(blank=True, null=True)),
                ('usuario', models.CharField(max_length=30)),
                ('especie', models.CharField(max_length=30)),
                ('variedad', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'pago',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id_pais', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'pais',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id_provincia', models.IntegerField(primary_key=True, serialize=False)),
                ('des_provincia', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'provincia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Puntos',
            fields=[
                ('id_puntos', models.IntegerField(primary_key=True, serialize=False)),
                ('des_puntos', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'puntos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id_region', models.IntegerField(primary_key=True, serialize=False)),
                ('des_region', models.CharField(max_length=50)),
                ('region_id', models.IntegerField(unique=True)),
            ],
            options={
                'db_table': 'region',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id_rol', models.IntegerField(primary_key=True, serialize=False)),
                ('des_rol', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'rol',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id_solicitud', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_entrega', models.DateField(blank=True, null=True)),
                ('fecha_creacion', models.DateField()),
                ('fecha_de_termino', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'solicitud',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StockSobrante',
            fields=[
                ('id_stock', models.IntegerField(primary_key=True, serialize=False)),
                ('kilo', models.IntegerField(blank=True, null=True)),
                ('fecha_cosecha', models.DateField(blank=True, null=True)),
                ('fecha_entrada', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'stock_sobrante',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.IntegerField(primary_key=True, serialize=False)),
                ('run_usuario', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=50)),
                ('ap_paterno', models.CharField(max_length=25)),
                ('ap_materno', models.CharField(max_length=25)),
                ('fecha_nac', models.DateField()),
                ('email', models.CharField(max_length=250)),
                ('direccion', models.CharField(max_length=150)),
                ('num_celular', models.IntegerField()),
                ('clave', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'usuario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Variedad',
            fields=[
                ('id_variedad', models.IntegerField(primary_key=True, serialize=False)),
                ('des_variedad', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'variedad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VentaLocal',
            fields=[
                ('id_venta_local', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'venta_local',
                'managed': False,
            },
        ),
    ]
