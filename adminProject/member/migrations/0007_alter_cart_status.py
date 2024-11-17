# Generated by Django 4.2.5 on 2024-11-12 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0006_alter_cart_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.CharField(choices=[('chuaThanhToan', 'Chưa thanh toán'), ('daThanhToan', 'Đã thanh toán'), ('dangGiaoHang', 'Đang giao hàng'), ('daGiaoHang', 'Đã giao hàng')], default='chuaThanhToan', max_length=20),
        ),
    ]