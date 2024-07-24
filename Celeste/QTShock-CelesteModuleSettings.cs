namespace Celeste.Mod.QTShock_Celeste;
public class QTShock_CelesteModuleSettings : EverestModuleSettings {

        [SettingName("Toggle Mod")]
        [SettingSubText("Toggles the mod on and off.")]
        public bool Toggle { get; set; } = true;

        [SettingRange(0, 4)]
        [SettingName("Shocker")]
        [SettingSubText("Index of the shocker to use. (0 is 1st shocker)")]
        public int Shocker { get; set; } = 0;

        [SettingRange(1, 99)]
        [SettingName("Strength")]
        public int Strength { get; set; } = 40;

        [SettingName("Type")]
        public EnumType Type { get; set; } = EnumType.Shock;
        public enum EnumType {
            Beep,
            Vibrate,
            Shock
        }
}