class TelegramBotRouter:
    """
    A database router to control operations on Telegram bot models.
    """

    def db_for_read(self, model, **hints):
        """Direct read operations to the appropriate database."""
        if model._meta.app_label == 'telegram_bot':
            return 'telegram_bot'  # خواندن داده از دیتابیس ربات
        return 'default'  # سایر مدل‌ها از دیتابیس پیش‌فرض خوانده می‌شوند

    def db_for_write(self, model, **hints):
        """Direct write operations to the appropriate database."""
        if model._meta.app_label == 'telegram_bot':
            return 'telegram_bot'  # نوشتن داده در دیتابیس ربات
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """Allow relations only within the same database."""
        if (
            obj1._meta.app_label == 'telegram_bot'
            or obj2._meta.app_label == 'telegram_bot'
        ):
            return True  # اجازه روابط بین مدل‌های دیتابیس ربات
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure that migrations are directed to the correct database."""
        if app_label == 'telegram_bot':
            return db == 'telegram_bot'  # مهاجرت مدل‌های ربات به دیتابیس مربوطه
        return db == 'default'  # سایر مهاجرت‌ها به دیتابیس پیش‌فرض
