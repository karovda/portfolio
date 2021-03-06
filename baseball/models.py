# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.urls import reverse


class PlayerInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    fplayerid = models.IntegerField(blank=True, null=True)
    first_year = models.IntegerField(blank=True, null=True)
    last_year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "player_info"

    def get_absolute_url(self):
        return reverse("baseball:player-detail", args=[str(self.id)])

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "first_year": self.first_year,
            "last_year": self.last_year,
        }


class Batters(models.Model):
    id = models.IntegerField(primary_key=True)
    team = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    g = models.IntegerField(blank=True, null=True)
    pa = models.IntegerField(blank=True, null=True)
    hr = models.IntegerField(blank=True, null=True)
    r = models.IntegerField(blank=True, null=True)
    rbi = models.IntegerField(blank=True, null=True)
    sb = models.IntegerField(blank=True, null=True)
    bb_rate = models.FloatField(blank=True, null=True)
    k_rate = models.FloatField(blank=True, null=True)
    iso = models.FloatField(blank=True, null=True)
    babip = models.FloatField(blank=True, null=True)
    avg = models.FloatField(blank=True, null=True)
    obp = models.FloatField(blank=True, null=True)
    slg = models.FloatField(blank=True, null=True)
    woba = models.FloatField(blank=True, null=True)
    wrc_plus = models.IntegerField(blank=True, null=True)
    ev = models.FloatField(blank=True, null=True)
    bsr = models.FloatField(blank=True, null=True)
    off = models.FloatField(blank=True, null=True)
    def_field = models.FloatField(
        db_column="def", blank=True, null=True
    )  # Field renamed because it was a Python reserved word.
    war = models.FloatField(blank=True, null=True)
    war_per_600 = models.FloatField(blank=True, null=True)
    player = models.ForeignKey(
        "PlayerInfo", on_delete=models.RESTRICT, blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "batters"


class Pitchers(models.Model):
    id = models.IntegerField(primary_key=True)
    team = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    w = models.IntegerField(blank=True, null=True)
    l = models.IntegerField(blank=True, null=True)
    sv = models.IntegerField(blank=True, null=True)
    g = models.IntegerField(blank=True, null=True)
    gs = models.IntegerField(blank=True, null=True)
    ip = models.FloatField(blank=True, null=True)
    k_per_9 = models.FloatField(blank=True, null=True)
    bb_per_9 = models.FloatField(blank=True, null=True)
    hr_per_9 = models.FloatField(blank=True, null=True)
    babip = models.FloatField(blank=True, null=True)
    lob_rate = models.FloatField(blank=True, null=True)
    gb_rate = models.FloatField(blank=True, null=True)
    hr_per_fb = models.FloatField(blank=True, null=True)
    ev = models.FloatField(blank=True, null=True)
    era = models.FloatField(blank=True, null=True)
    fip = models.FloatField(blank=True, null=True)
    xfip = models.FloatField(blank=True, null=True)
    war = models.FloatField(blank=True, null=True)
    war_per_200 = models.FloatField(blank=True, null=True)
    player = models.ForeignKey(
        "PlayerInfo", on_delete=models.RESTRICT, blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "pitchers"


class CareerStats(models.Model):
    id = models.IntegerField(primary_key=True)
    default_batting = models.IntegerField(blank=True, null=True)
    bat_career = models.FloatField(blank=True, null=True)
    bat_peak = models.FloatField(blank=True, null=True)
    bat_avg = models.FloatField(blank=True, null=True)
    career_pas = models.IntegerField(blank=True, null=True)
    peak_pas = models.IntegerField(blank=True, null=True)
    bat_rate_career = models.FloatField(blank=True, null=True)
    bat_rate_peak = models.FloatField(blank=True, null=True)
    bat_rate_avg = models.FloatField(blank=True, null=True)
    pit_career = models.FloatField(blank=True, null=True)
    pit_peak = models.FloatField(blank=True, null=True)
    pit_avg = models.FloatField(blank=True, null=True)
    career_ip = models.FloatField(blank=True, null=True)
    peak_ip = models.FloatField(blank=True, null=True)
    pit_rate_career = models.FloatField(blank=True, null=True)
    pit_rate_peak = models.FloatField(blank=True, null=True)
    pit_rate_avg = models.FloatField(blank=True, null=True)
    player = models.ForeignKey(
        "PlayerInfo", on_delete=models.RESTRICT, blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "career_stats"


class StatDescriptions(models.Model):
    id = models.IntegerField(primary_key=True)
    description_type = models.TextField(blank=False, null=False, default="")
    bat_career = models.TextField(blank=False, null=False, default="")
    bat_peak = models.TextField(blank=False, null=False, default="")
    bat_avg = models.TextField(blank=False, null=False, default="")
    bat_rate_career = models.TextField(blank=False, null=False, default="")
    bat_rate_peak = models.TextField(blank=False, null=False, default="")
    bat_rate_avg = models.TextField(blank=False, null=False, default="")
    pit_career = models.TextField(blank=False, null=False, default="")
    pit_peak = models.TextField(blank=False, null=False, default="")
    pit_avg = models.TextField(blank=False, null=False, default="")
    pit_rate_career = models.TextField(blank=False, null=False, default="")
    pit_rate_peak = models.TextField(blank=False, null=False, default="")
    pit_rate_avg = models.TextField(blank=False, null=False, default="")
    career_ip = models.TextField(blank=False, null=False, default="")
    career_pas = models.TextField(blank=False, null=False, default="")
    peak_pas = models.TextField(blank=False, null=False, default="")
    peak_ip = models.TextField(blank=False, null=False, default="")

    class Meta:
        managed = True
        db_table = "stat_descriptions"
        verbose_name_plural = "Stat descriptions"

    def __str__(self):
        return self.description_type
