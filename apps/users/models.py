from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


class UserProfile(AbstractUser):
    """
            CREATE TABLE `lr_user` (
          `id` int(11) NOT NULL COMMENT '用户表：包括后台管理员、商家会员和普通会员',
          `name` varchar(20) NOT NULL COMMENT '登陆账号',
          `uname` varchar(10) DEFAULT NULL COMMENT '昵称',
          `pwd` varchar(50) NOT NULL COMMENT 'MD5密码',
          `addtime` int(11) NOT NULL DEFAULT '0' COMMENT '创建日期',
          `jifen` float(11,0) DEFAULT '0' COMMENT '积分',
          `photo` varchar(255) DEFAULT NULL COMMENT '头像',
          `tel` char(15) DEFAULT NULL COMMENT '手机',
          `qq_id` varchar(20) NOT NULL DEFAULT '0' COMMENT 'qq',
          `email` varchar(50) DEFAULT NULL COMMENT '邮箱',
          `sex` tinyint(2) NOT NULL DEFAULT '0' COMMENT '性别',
          `del` tinyint(2) NOT NULL DEFAULT '0' COMMENT '状态',
          `openid` varchar(50) NOT NULL COMMENT '授权ID',
          `source` varchar(10) NOT NULL COMMENT '第三方平台(微信，QQ)'
        ) ENGINE=MyISAM DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;
    """
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="登陆账号")
    portrait = models.CharField(max_length=255, null=True, blank=True, verbose_name="头像")
    openid = models.CharField(max_length=50, null=True, blank=True, verbose_name="授权ID")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
