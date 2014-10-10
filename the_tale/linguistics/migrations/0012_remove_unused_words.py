# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

REMOVED_WORDS = [
u'хомячья шкурка',
u'дряхлый доспех',
u'Афины',
u'лягушачья икра',
u'разбитый посох',
u'сера',
u'копье',
u'хищный кустик',
u'монокль',
u'живот',
u'жгучая роса',
u'волчий хвост',
u'погремушка',
u'астральный охотник',
u'свинья',
u'скарабей',
u'хищный хомяк',
u'яд скорпиона',
u'отравленный кинжал',
u'глина',
u'рыцарь',
u'шакал',
u'метла',
u'горсть светлячков',
u'Рига',
u'ресурс_2',
u'шкура волка',
u'берсерк',
u'Бородино',
u'единорог',
u'проклятое кольцо',
u'медвежья лапа',
u'вольница',
u'сломанный механизм',
u'супер сила',
u'Тагил',
u'узкие штаны',
u'мясо оленя',
u'боевая помада',
u'орк',
u'пергамент',
u'блюститель природы',
u'яд змеи',
u'человек',
u'дух леса',
u'вещь',
u'эссенция ярости',
u'убивалка',
u'кусок сыра',
u'дырявый кошель',
u'росток радуги',
u'каска',
u'молот атеистов',
u'ножницы',
u'василиск',
u'молитвенник',
u'кость мертвеца',
u'мусорника',
u'Магадан',
u'домашний поползень',
u'смерч',
u'дварф',
u'одержалка',
u'кинжал',
u'краска',
u'земля',
u'какой-то текст',
u'текст текст текст',
u'любой текст',
u'головастик',
u'налетчик',
u'рукавица',
u'олень',
u'Простоквашино',
u'звездный венок',
u'осколок прошлого',
u'болотный сапог',
u'щупальце',
u'жвала богомола',
u'разбитая колба',
u'налобный рог',
u'убийца',
u'одержимый колдун',
u'полоумный маг',
u'медведь',
u'удилище',
u'гоблин',
u'дубина',
u'пламенный воротник',
u'зеркальце',
u'святой город',
u'маньяк-извращенец',
u'село',
u'Уфа',
u'рваные трусы',
u'кабан-секач',
u'неупокоенный',
u'огненная лиса',
u'кожаные штаны',
u'голь',
u'антенк поползня',
u'лапоть',
u'предприимчивый',
u'мой',
u'тулуп поползня',
u'колба от яда',
u'ресурс_1',
u'ползун',
u'сердце ползуна',
u'саранча',
u'трупик осы',
u'волчий клык',
u'рыжий хвост',
u'оскорбленная эльфийка',
u'лапа богомола',
u'пятачок',
u'письмо',
u'доспех из чешуек дракона',
u'длинная фраза',
u'чучело',
u'дварф-изгнанник',
u'глиняные штаны',
u'заблудший шаман',
u'волшебное зернышко',
u'меч',
u'орк-изгнанник',
u'высушенный скарабей',
u'жираф',
u'рванье',
u'сломанная стрела',
u'мертвый головастик',
u'пугало',
u'охотник за реагентами',
u'благородный разбойник',
u'лук',
u'крысиный хвостик',
u'механический дракончик',
u'сверкающий плащ',
u'эссенция ума',
u'поддельный амулет',
u'живой корень',
u'окно',
u'меч справедливости',
u'макароны',
u'химический мусорник',
u'подкова',
u'святыня',
u'концентрированная ярость',
u'призрачный хвост',
u'астральный пепел',
u'призрачный волк',
u'шкура шакала',
u'кровь упыря',
u'антенк',
u'аристократ',
u'осиное жало',
u'пиявка',
u'бродячий дуб',
u'антеннка поползня',
u'слон',
u'колония',
u'Минск',
u'оса',
u'резиновая перчатка',
u'курорт',
u'приведение',
u'добротные штаны',
u'магическая броня',
u'захолустье',
u'замок',
u'ядро',
u'присоска',
u'Чебоксары',
u'хутор',
u'волшебная лампа',
u'рунный топор',
u'сбежавший эксперимент',
u'пепельница',
u'транспортный узел',
u'пристанище',
u'нож',
u'огнемет',
u'странная жидкость',
u'концентрированая ярость',
u'сломаный меч',
u'упырь',
u'кабаний клык',
u'корона',
u'красная книга',
u'джинн',
u'шарик скарабея',
u'дырявая шапка',
u'слизкий сапог',
u'Вилейка',
u'ожившее пугало',
u'полис',
u'огненный плащ',
u'кикимора',
u'одичавший светлячка',
u'шестеренка',
u'галстук из щупальца',
u'бандит',
u'олений рог',
u'мертвая пиявка',
u'пасть росянки',
u'мозговой слизень',
u'жало скорпиона',
u'одичавшая одежда',
u'Барановичи',
u'гигантская росянка',
u'Чугуево',
u'политический центр',
u'бесхозный голем',
u'потный плащ',
u'голова гидры',
u'призрак',
u'кусок кожи с клеймом',
u'чешуйка дракончика',
u'чудовище',
u'гидра',
u'крыса',
u'пепел',
u'роба',
u'стальные трусы',
u'пустынный дракончик',
u'призрачный наплечник',
u'шкура медведя',
u'форт',
u'эльф',
u'сердце леса',
u'волшебный посох',
u'разумный обруч',
u'ряска',
u'большой-большой меч',
u'шкура оленя',
u'застывшее пламя',
u'цепь',
u'джокер',
u'чашка',
u'торговый центр',
u'последний вздох',
u'шайтан',
u'сабля',
u'карточный шулер',
u'гусь',
u'механический голем',
u'неистовый сектант',
u'рваная перчатка',
u'слизь',
u'герой',
u'богомол',
u'героиня',
u'белый халат',
u'пшеничный колосок',
u'разбитая лампа',
u'молот',
u'волк',
u'скорпион',
u'зебра',
u'саламандра',
u'шакалий хвост',
u'город мастеров',
u'борода дварфа',
u'эссенция ветра',
u'дырявое ведро',
u'мутировавший гоблин',
u'дрова',
u'город',
u'боец',
u'выеденный плащ',
u'желудь',
u'сломаный механизм',
u'жало',
u'привидение',
u'мечта',
u'борец за справедливость',
u'варенье',
u'окаменевшая птичка',
u'волшебные штаны',
u'портки',
u'посуда алхимика',
u'русалка',
u'химический доспех',
u'светлячёк',
u'ветреный сапог',
u'пропитанный химией плащ',
u'мемориал',
u'перегонный куб',
u'тонкая перчатка',
u'гремучая змея',
u'праздную-инфинитив',
u'примерил-инфинитив',
u'расспрашиваю-инфинитив',
u'направляюсь-инфинитив',
u'подскользнулся-инфинитив',
u'вдохнул-инфинитив',
u'присвоил-инфинитив',
u'пустил-инфинитив',
u'погибаю-инфинитив',
u'наградил-инфинитив',
u'примечусь-инфинитив',
u'изменил-инфинитив',
u'достаюсь-инфинитив',
u'предпочел-инфинитив',
u'рассчитываю-инфинитив',
u'отскочил-инфинитив',]

class Migration(DataMigration):

    def forwards(self, orm):
        orm['linguistics.Word'].objects.filter(normal_form__in=REMOVED_WORDS).delete()

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        u'accounts.account': {
            'Meta': {'ordering': "['nick']", 'object_name': 'Account'},
            'action_id': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '128', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'active_end_at': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'ban_forum_end_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(1970, 1, 1, 0, 0)', 'db_index': 'True'}),
            'ban_game_end_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(1970, 1, 1, 0, 0)', 'db_index': 'True'}),
            'clan': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['clans.Clan']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(1970, 1, 1, 0, 0)', 'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_bot': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_fast': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_news_remind_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(1970, 1, 1, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'might': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'new_messages_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'nick': ('django.db.models.fields.CharField', [], {'default': "u''", 'unique': 'True', 'max_length': '128', 'db_index': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'permanent_purchases': ('django.db.models.fields.TextField', [], {'default': "'[]'"}),
            'personal_messages_subscription': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'premium_end_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(1970, 1, 1, 0, 0)', 'db_index': 'True'}),
            'premium_expired_notification_send_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(1970, 1, 1, 0, 0)', 'db_index': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '4096', 'null': 'True'}),
            'referer_domain': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '256', 'null': 'True', 'db_index': 'True'}),
            'referral_of': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['accounts.Account']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'referrals_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(1970, 1, 1, 0, 0)', 'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"})
        },
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
        u'clans.clan': {
            'Meta': {'object_name': 'Clan'},
            'abbr': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '5'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '2024'}),
            'forum_subcategory': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['forum.SubCategory']", 'on_delete': 'models.PROTECT'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'members_number': ('django.db.models.fields.IntegerField', [], {}),
            'motto': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'forum.category': {
            'Meta': {'object_name': 'Category'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '32', 'db_index': 'True'})
        },
        u'forum.subcategory': {
            'Meta': {'object_name': 'SubCategory'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['forum.Category']", 'on_delete': 'models.PROTECT'}),
            'closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(1970, 1, 1, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "u''"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_poster': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['accounts.Account']"}),
            'last_thread': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['forum.Thread']"}),
            'last_thread_created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(1970, 1, 1, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'posts_count': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'restricted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'threads_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'uid': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '16', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(1970, 1, 1, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'})
        },
        u'forum.thread': {
            'Meta': {'object_name': 'Thread'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['accounts.Account']"}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(1970, 1, 1, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'important': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'last_poster': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['accounts.Account']"}),
            'posts_count': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'subcategory': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['forum.SubCategory']", 'on_delete': 'models.PROTECT'}),
            'technical': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(1970, 1, 1, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'})
        },
        u'linguistics.template': {
            'Meta': {'object_name': 'Template'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.Account']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data': ('django.db.models.fields.TextField', [], {}),
            'errors_status': ('rels.django.RelationIntegerField', [], {'default': '0', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('rels.django.RelationIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['linguistics.Template']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'raw_template': ('django.db.models.fields.TextField', [], {}),
            'state': ('rels.django.RelationIntegerField', [], {'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'linguistics.word': {
            'Meta': {'unique_together': "(('normal_form', 'type', 'state'),)", 'object_name': 'Word'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'forms': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'normal_form': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['linguistics.Word']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'state': ('rels.django.RelationIntegerField', [], {'db_index': 'True'}),
            'type': ('rels.django.RelationIntegerField', [], {'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'used_in_ingame_templates': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'used_in_onreview_templates': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'used_in_status': ('rels.django.RelationIntegerField', [], {'default': '2', 'db_index': 'True'})
        }
    }

    complete_apps = ['linguistics']
    symmetrical = True
