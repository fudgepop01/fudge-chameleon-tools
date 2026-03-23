/*
 * This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
 */
import KaitaiStream from 'kaitai-struct/KaitaiStream'

export class GenericGenObject {
  _is_le?: boolean;

  constructor(
    readonly _io: KaitaiStream,
    readonly _parent?: unknown,
    readonly _root?: GenericGenObject,
  ) {
    this._root ??= this;

    this._read();
  }

  _read() {
    if ((this.ofs as any) < 0) {
      this.saveOfs = (this._io.readBytes(0)) as any
    }
    this.obj = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
  }

  private _ofs: number;
  get ofs(): number {
    if (typeof this._ofs !== 'undefined')
      return this._ofs;
    this._ofs = ((this._io as any).pos) as any
    return this._ofs;
  }

  private _data: GenericGenObject.GenesysGenEnvironmentKeyframeVfx | undefined | GenericGenObject.GenesysGenGameUnlockList | undefined | GenericGenObject.GenesysGenGameplayMilestoneEntry | undefined | GenericGenObject.GenesysGenTextStyleTextStyleLocale | undefined | GenericGenObject.GenesysGenPerk | undefined | GenericGenObject.GenesysGenGameplayMilestone | undefined | GenericGenObject.GenesysGenVfxSpotEffectSequenceItem | undefined | GenericGenObject.GenesysGenHeatLevel | undefined | GenericGenObject.GenesysGenUielementPrototypeImage | undefined | GenericGenObject.GenesysGenCarSelectDataSequences | undefined | GenericGenObject.GenesysGenUielementPrototypeLabel | undefined | GenericGenObject.GenesysGenWchideBehaviour | undefined | GenericGenObject.GenesysGenPerkLevel | undefined | GenericGenObject.GenesysGenGameplayTriggerOutputSequenceOutput | undefined | GenericGenObject.GenesysGenThankyouMapping | undefined | GenericGenObject.GenesysGenEventList | undefined | GenericGenObject.GenesysGenStoreItem | undefined | GenericGenObject.GenesysGenLightCone | undefined | GenericGenObject.GenesysGenEntitlement | undefined | GenericGenObject.GenesysGenTeflonSlickWeapon | undefined | GenericGenObject.GenesysGenEnvironmentTimeline | undefined | GenericGenObject.GenesysGenSpikeStripBlowoutUpgrade | undefined | GenericGenObject.GenesysGenRoadBlockLayer | undefined | GenericGenObject.GenesysGenPhysicalExplosionGameplayExplosion | undefined | GenericGenObject.GenesysGenUielementElementStack | undefined | GenericGenObject.GenesysGenEnvironmentKeyframe | undefined | GenericGenObject.GenesysGenArcLightConeUpgrade | undefined | GenericGenObject.GenesysGenSequenceItemModulatingDoubleValue | undefined | GenericGenObject.GenesysGenAiplayerType | undefined | GenericGenObject.GenesysGenSequenceItem | undefined | GenericGenObject.GenesysGenJumpTimelineController | undefined | GenericGenObject.GenesysGenGameplayTrigger | undefined | GenericGenObject.GenesysGenStorePack | undefined | GenericGenObject.GenesysGenLightBaseFlashPattern | undefined | GenericGenObject.GenesysGenPhysicalDefinition | undefined | GenericGenObject.GenesysGenHeatLevelCopType | undefined | GenericGenObject.GenesysGenSequence | undefined | GenericGenObject.GenesysGenBusMixerChannelSequenceItem | undefined | GenericGenObject.GenesysGenUielementBase | undefined | GenericGenObject.GenesysGenGameUnlockEvent | undefined | GenericGenObject.GenesysGenAnimationSequenceItem | undefined | GenericGenObject.GenesysGenWeaponList | undefined | GenericGenObject.GenesysGenUielementPrototypeScrollingTextString | undefined | GenericGenObject.GenesysGenCameraGameplayShakeEffectRotationAxisParams | undefined | GenericGenObject.GenesysGenOfflineEvent | undefined | GenericGenObject.GenesysGenGameModeScoreOverride | undefined | GenericGenObject.GenesysGenPostFxstate | undefined | GenericGenObject.GenesysGenPhysicalExplosion | undefined | GenericGenObject.GenesysGenCoronaBeam | undefined | GenericGenObject.GenesysGenSilentLaunchWeaponUpgrade | undefined | GenericGenObject.GenesysGenUielementScrollableLabel | undefined | GenericGenObject.GenesysGenPhysicalExplosionNonRaceCarExplosion | undefined | GenericGenObject.GenesysGenUimaterial | undefined | GenericGenObject.GenesysGenPostFxKeyframeStereo3d | undefined | GenericGenObject.GenesysGenSlowMoSequenceItem | undefined | GenericGenObject.GenesysGenPostFxKeyframeGeneral | undefined | GenericGenObject.GenesysGenPhysicsSequenceItemPhysicsDoubleValue | undefined | GenericGenObject.GenesysGenUielementPrototypeImageOpacity | undefined | GenericGenObject.GenesysGenWcpathAnimationBehaviour | undefined | GenericGenObject.GenesysGenUielementMask | undefined | GenericGenObject.GenesysGenEnvironmentKeyframeLightRig | undefined | GenericGenObject.GenesysGenWaveSequenceItemFade | undefined | GenericGenObject.GenesysGenCameraGameplayShakeEffectTranslation | undefined | GenericGenObject.GenesysGenPhysicalDefinitionRigidBodyCylinderVolume | undefined | GenericGenObject.GenesysGenUielementPrototypeLabelString | undefined | GenericGenObject.GenesysGenCameraShakeSequenceItem | undefined | GenericGenObject.GenesysGenEventArenaData | undefined | GenericGenObject.GenesysGenCorona | undefined | GenericGenObject.GenesysGenScoreViewModel | undefined | GenericGenObject.GenesysGenJammerWeapon | undefined | GenericGenObject.GenesysGenThermalVisionMode | undefined | GenericGenObject.GenesysGenNucleusGrantMappingsListMapping | undefined | GenericGenObject.GenesysGenWcvfxBehaviourCoronas | undefined | GenericGenObject.GenesysGenEnvironmentKeyframeClouds | undefined | GenericGenObject.GenesysGenNucleusEntitlementTags | undefined | GenericGenObject.GenesysGenPhysicalDefinitionRigidBodyConvexHullVolume | undefined | GenericGenObject.GenesysGenGameRule | undefined | GenericGenObject.GenesysGenMixerChannel | undefined | GenericGenObject.GenesysGenWcplaySoundBehaviourPropSurfaceSound | undefined | GenericGenObject.GenesysGenEnvironmentKeyframeFog | undefined | GenericGenObject.GenesysGenUielementPrototypeLabelTextProperties | undefined | GenericGenObject.GenesysGenDeviceGrantUpgradePackage | undefined | GenericGenObject.GenesysGenNitrousBurningGameRule | undefined | GenericGenObject.GenesysGenWcremoveWorldEntityBehaviour | undefined | GenericGenObject.GenesysGenUielementPrototypeScrollingText | undefined | GenericGenObject.GenesysGenPhysicalExplosionRaceCarOnGroundExplosion | undefined | GenericGenObject.GenesysGenHelicopterWeapon | undefined | GenericGenObject.GenesysGenRolloutWeaponData | undefined | GenericGenObject.GenesysGenNucleusGrantMappingsList | undefined | GenericGenObject.GenesysGenSearchlightBehaviour | undefined | GenericGenObject.GenesysGenCoronaFlare | undefined | GenericGenObject.GenesysGenOfflineEventCustomChevrons | undefined | GenericGenObject.GenesysGenUicolour | undefined | GenericGenObject.GenesysGenEnvironmentKeyframeSky | undefined | GenericGenObject.GenesysGenUitechnique | undefined | GenericGenObject.GenesysGenWcvfxBehaviourLights | undefined | GenericGenObject.GenesysGenGameplayTriggerOutput | undefined | GenericGenObject.GenesysGenUielementMiniMap | undefined | GenericGenObject.GenesysGenUielementBaseRenderingData | undefined | GenericGenObject.GenesysGenGameMode | undefined | GenericGenObject.GenesysGenPhysicalDefinitionRigidBody | undefined | GenericGenObject.GenesysGenBehaviour | undefined | GenericGenObject.GenesysGenRoadBlockDefinition | undefined | GenericGenObject.GenesysGenEventArena | undefined | GenericGenObject.GenesysGenTextStyle | undefined | GenericGenObject.GenesysGenUielementPrototypeShape | undefined | GenericGenObject.GenesysGenScoreViewModelScoreData | undefined | GenericGenObject.GenesysGenRoadBlockLayerItem | undefined | GenericGenObject.GenesysGenGameRank | undefined | GenericGenObject.GenesysGenEnvironmentKeyframeCamera | undefined | GenericGenObject.GenesysGenGamePack | undefined | GenericGenObject.GenesysGenEventTriggerSequenceItem | undefined | GenericGenObject.GenesysGenNitrousEarningGameRule | undefined | GenericGenObject.GenesysGenSnapToWorldBehaviour | undefined | GenericGenObject.GenesysGenEnvironmentKeyframeWeather | undefined | GenericGenObject.GenesysGenNucleusEntitlementTag | undefined | GenericGenObject.GenesysGenThermalVisionModeProperties | undefined | GenericGenObject.GenesysGenFastLaunchWeaponUpgrade | undefined | GenericGenObject.GenesysGenWeaponUpgrade | undefined | GenericGenObject.GenesysGenScoringAction | undefined | GenericGenObject.GenesysGenEnvironmentKeyframeMiniDof | undefined | GenericGenObject.GenesysGenDustStormMinimapUpgrade | undefined | GenericGenObject.GenesysGenWeapon | undefined | GenericGenObject.GenesysGenUilayoutInstanceParamsTimelineParameters | undefined | GenericGenObject.GenesysGenWcsequenceBehaviour | undefined | GenericGenObject.GenesysGenWcvfxBehaviour | undefined | GenericGenObject.StringBase | undefined | GenericGenObject.GenesysGenRoadblockInstance | undefined | GenericGenObject.GenesysGenSpikeStripWeapon | undefined | GenericGenObject.RwMathVpuVector4 | undefined | GenericGenObject.GenesysGenUielementElementStackTemplate | undefined | GenericGenObject.GenesysGenMakePhysicalBehaviour | undefined | GenericGenObject.RwMathVpuVector3 | undefined | GenericGenObject.GenesysGenPostFxstateColourCubeSettings | undefined | GenericGenObject.GenesysGenUielementMoviePlayer | undefined | GenericGenObject.GenesysGenLightBase | undefined | GenericGenObject.GenesysGenUielementMoviePlayerDimensions | undefined | GenericGenObject.GenesysGenSpeedbreakerWeapon | undefined | GenericGenObject.GenesysGenEnvironmentTimelineTimelineKeyframe | undefined | GenericGenObject.GenesysGenUilayoutInstanceParams | undefined | GenericGenObject.GenesysGenUielementBaseBehaviour | undefined | GenericGenObject.GenesysGenPostFxKeyframeDepthOfField | undefined | GenericGenObject.GenesysGenPhysicalDefinitionRigidBodyBoxVolume | undefined | GenericGenObject.GenesysGenLayoutSequenceItem | undefined | GenericGenObject.RwMathVpuMatrix44affine | undefined | GenericGenObject.GenesysGenUielementBaseTimelineBehaviour | undefined | GenericGenObject.GenesysGenUilayoutInstanceParamsTransformComponents | undefined | GenericGenObject.GenesysGenExtraAmmoWeaponUpgrade | undefined | GenericGenObject.GenesysGenUielementScrollableLabelString | undefined | GenericGenObject.GenesysGenPostFxKeyframe | undefined | GenericGenObject.GenesysGenEnvironmentKeyframeHeatHaze | undefined | GenericGenObject.GenesysGenSetVisionModeTypeSequenceItem | undefined | GenericGenObject.RwRgba | undefined | GenericGenObject.GenesysGenPerformanceUpgradePackage | undefined | GenericGenObject.GenesysGenWeaponRechargeData | undefined | GenericGenObject.GenesysGenBusMixerChannelSequenceItemBusMixerChannelDoubleValue | undefined | GenericGenObject.GenesysGenUielementPrototypeScrollingTextTextProperties | undefined | GenericGenObject.GenesysObjCollection | undefined | GenericGenObject.GenesysGenSequenceTimelineController | undefined | GenericGenObject.GenesysGenCustomChevron | undefined | GenericGenObject.GenesysGenPostFxsequenceItem | undefined | GenericGenObject.GenesysGenImpactDamageGameRule | undefined | GenericGenObject.GenesysGenAddBehaviourSequenceItem | undefined | GenericGenObject.GenesysGenPhysicalDefinitionRigidBodySphereVolume | undefined | GenericGenObject.GenesysGenMixingGroup | undefined | GenericGenObject.RwMathVpuVector2 | undefined | GenericGenObject.GenesysGenRollout | undefined | GenericGenObject.GenesysGenFlashHeadlightsWeapon | undefined | GenericGenObject.GenesysGenGameUnlockMilestone | undefined | GenericGenObject.GenesysGenMixerChannelPriority | undefined | GenericGenObject.GenesysGenWcplaySoundBehaviour | undefined | GenericGenObject.GenesysGenUilayout | undefined | GenericGenObject.GenesysGenCoronaGlow | undefined | GenericGenObject.GenesysGenEventLocation | undefined | GenericGenObject.GenesysGenHypoxParticlesWeaponUpgrade | undefined | GenericGenObject.GenesysGenUielementScrollableLabelTextProperties | undefined | GenericGenObject.GenesysGenPostFxKeyframeBloom | undefined | GenericGenObject.GenesysGenHudStyleSequenceItem | undefined | GenericGenObject.GenesysGenPhysicalExplosionRaceCarInAirExplosion | undefined | GenericGenObject.GenesysGenCarSelectData | undefined | GenericGenObject.GenesysGenUielementPrototypeImageTintProperties | undefined | GenericGenObject.GenesysGenVisionMode | undefined | GenericGenObject.GenesysGenUicamera | undefined | GenericGenObject.GenesysGenCameraGameplayShakeEffect | undefined | GenericGenObject.GenesysGenGameplayTriggerInput | undefined | GenericGenObject.GenesysGenWcvfxBehaviourSpotEffects | undefined | GenericGenObject.GenesysGenWaveSequenceItem | undefined | GenericGenObject.GenesysGenAiplayerInstance | undefined | GenericGenObject.GenesysGenUielementBaseTimeline | undefined | GenericGenObject.GenesysGenEnvironmentTimelineSequenceItem | undefined | GenericGenObject.GenesysGenFlashBangWeapon | undefined | GenericGenObject.GenesysGenGrenadeWeapon | undefined | GenericGenObject.GenesysGenApplyVehicleKickSequenceItem | undefined | GenericGenObject.GenesysGenSmokeScreenWeapon | undefined | GenericGenObject.GenesysGenChevron | undefined | GenericGenObject.GenesysGenPhysicsSequenceItem | undefined | GenericGenObject.GenesysGenImpactProtectionGameRule | undefined | GenericGenObject.GenesysGenCoronaEnvMapGlow | undefined | GenericGenObject.GenesysGenUielementMainMap | undefined | GenericGenObject.GenesysGenCameraGameplayShakeEffectTranslationAxisParams | undefined | GenericGenObject.GenesysGenEvent | undefined | GenericGenObject.GenesysGenUpgradePackage | undefined | GenericGenObject.GenesysGenSoundDistanceFalloff | undefined | GenericGenObject.GenesysGenMineWeapon | undefined | GenericGenObject.GenesysGenUielementBaseEffectConstant | undefined | GenericGenObject.GenesysGenGameUnlock | undefined | GenericGenObject.GenesysGenWcpathAnimationBehaviourAnimationPath | undefined | GenericGenObject.GenesysGenThankYouScreenItem | undefined | GenericGenObject.GenesysGenOnlineEvent | undefined | GenericGenObject.GenesysGenLightPoint | undefined | GenericGenObject.GenesysGenStorePackList | undefined | GenericGenObject.GenesysGenCameraGameplayShakeEffectRotation | undefined | GenericGenObject.GenesysGenPostFxstateValueModifier | undefined | GenericGenObject.GenesysGenPostFxKeyframeVignette | undefined | GenericGenObject.GenesysGenSpikeStripBodyBlowUpgrade | undefined | undefined;
  get data(): GenericGenObject.GenesysGenEnvironmentKeyframeVfx | undefined | GenericGenObject.GenesysGenGameUnlockList | undefined | GenericGenObject.GenesysGenGameplayMilestoneEntry | undefined | GenericGenObject.GenesysGenTextStyleTextStyleLocale | undefined | GenericGenObject.GenesysGenPerk | undefined | GenericGenObject.GenesysGenGameplayMilestone | undefined | GenericGenObject.GenesysGenVfxSpotEffectSequenceItem | undefined | GenericGenObject.GenesysGenHeatLevel | undefined | GenericGenObject.GenesysGenUielementPrototypeImage | undefined | GenericGenObject.GenesysGenCarSelectDataSequences | undefined | GenericGenObject.GenesysGenUielementPrototypeLabel | undefined | GenericGenObject.GenesysGenWchideBehaviour | undefined | GenericGenObject.GenesysGenPerkLevel | undefined | GenericGenObject.GenesysGenGameplayTriggerOutputSequenceOutput | undefined | GenericGenObject.GenesysGenThankyouMapping | undefined | GenericGenObject.GenesysGenEventList | undefined | GenericGenObject.GenesysGenStoreItem | undefined | GenericGenObject.GenesysGenLightCone | undefined | GenericGenObject.GenesysGenEntitlement | undefined | GenericGenObject.GenesysGenTeflonSlickWeapon | undefined | GenericGenObject.GenesysGenEnvironmentTimeline | undefined | GenericGenObject.GenesysGenSpikeStripBlowoutUpgrade | undefined | GenericGenObject.GenesysGenRoadBlockLayer | undefined | GenericGenObject.GenesysGenPhysicalExplosionGameplayExplosion | undefined | GenericGenObject.GenesysGenUielementElementStack | undefined | GenericGenObject.GenesysGenEnvironmentKeyframe | undefined | GenericGenObject.GenesysGenArcLightConeUpgrade | undefined | GenericGenObject.GenesysGenSequenceItemModulatingDoubleValue | undefined | GenericGenObject.GenesysGenAiplayerType | undefined | GenericGenObject.GenesysGenSequenceItem | undefined | GenericGenObject.GenesysGenJumpTimelineController | undefined | GenericGenObject.GenesysGenGameplayTrigger | undefined | GenericGenObject.GenesysGenStorePack | undefined | GenericGenObject.GenesysGenLightBaseFlashPattern | undefined | GenericGenObject.GenesysGenPhysicalDefinition | undefined | GenericGenObject.GenesysGenHeatLevelCopType | undefined | GenericGenObject.GenesysGenSequence | undefined | GenericGenObject.GenesysGenBusMixerChannelSequenceItem | undefined | GenericGenObject.GenesysGenUielementBase | undefined | GenericGenObject.GenesysGenGameUnlockEvent | undefined | GenericGenObject.GenesysGenAnimationSequenceItem | undefined | GenericGenObject.GenesysGenWeaponList | undefined | GenericGenObject.GenesysGenUielementPrototypeScrollingTextString | undefined | GenericGenObject.GenesysGenCameraGameplayShakeEffectRotationAxisParams | undefined | GenericGenObject.GenesysGenOfflineEvent | undefined | GenericGenObject.GenesysGenGameModeScoreOverride | undefined | GenericGenObject.GenesysGenPostFxstate | undefined | GenericGenObject.GenesysGenPhysicalExplosion | undefined | GenericGenObject.GenesysGenCoronaBeam | undefined | GenericGenObject.GenesysGenSilentLaunchWeaponUpgrade | undefined | GenericGenObject.GenesysGenUielementScrollableLabel | undefined | GenericGenObject.GenesysGenPhysicalExplosionNonRaceCarExplosion | undefined | GenericGenObject.GenesysGenUimaterial | undefined | GenericGenObject.GenesysGenPostFxKeyframeStereo3d | undefined | GenericGenObject.GenesysGenSlowMoSequenceItem | undefined | GenericGenObject.GenesysGenPostFxKeyframeGeneral | undefined | GenericGenObject.GenesysGenPhysicsSequenceItemPhysicsDoubleValue | undefined | GenericGenObject.GenesysGenUielementPrototypeImageOpacity | undefined | GenericGenObject.GenesysGenWcpathAnimationBehaviour | undefined | GenericGenObject.GenesysGenUielementMask | undefined | GenericGenObject.GenesysGenEnvironmentKeyframeLightRig | undefined | GenericGenObject.GenesysGenWaveSequenceItemFade | undefined | GenericGenObject.GenesysGenCameraGameplayShakeEffectTranslation | undefined | GenericGenObject.GenesysGenPhysicalDefinitionRigidBodyCylinderVolume | undefined | GenericGenObject.GenesysGenUielementPrototypeLabelString | undefined | GenericGenObject.GenesysGenCameraShakeSequenceItem | undefined | GenericGenObject.GenesysGenEventArenaData | undefined | GenericGenObject.GenesysGenCorona | undefined | GenericGenObject.GenesysGenScoreViewModel | undefined | GenericGenObject.GenesysGenJammerWeapon | undefined | GenericGenObject.GenesysGenThermalVisionMode | undefined | GenericGenObject.GenesysGenNucleusGrantMappingsListMapping | undefined | GenericGenObject.GenesysGenWcvfxBehaviourCoronas | undefined | GenericGenObject.GenesysGenEnvironmentKeyframeClouds | undefined | GenericGenObject.GenesysGenNucleusEntitlementTags | undefined | GenericGenObject.GenesysGenPhysicalDefinitionRigidBodyConvexHullVolume | undefined | GenericGenObject.GenesysGenGameRule | undefined | GenericGenObject.GenesysGenMixerChannel | undefined | GenericGenObject.GenesysGenWcplaySoundBehaviourPropSurfaceSound | undefined | GenericGenObject.GenesysGenEnvironmentKeyframeFog | undefined | GenericGenObject.GenesysGenUielementPrototypeLabelTextProperties | undefined | GenericGenObject.GenesysGenDeviceGrantUpgradePackage | undefined | GenericGenObject.GenesysGenNitrousBurningGameRule | undefined | GenericGenObject.GenesysGenWcremoveWorldEntityBehaviour | undefined | GenericGenObject.GenesysGenUielementPrototypeScrollingText | undefined | GenericGenObject.GenesysGenPhysicalExplosionRaceCarOnGroundExplosion | undefined | GenericGenObject.GenesysGenHelicopterWeapon | undefined | GenericGenObject.GenesysGenRolloutWeaponData | undefined | GenericGenObject.GenesysGenNucleusGrantMappingsList | undefined | GenericGenObject.GenesysGenSearchlightBehaviour | undefined | GenericGenObject.GenesysGenCoronaFlare | undefined | GenericGenObject.GenesysGenOfflineEventCustomChevrons | undefined | GenericGenObject.GenesysGenUicolour | undefined | GenericGenObject.GenesysGenEnvironmentKeyframeSky | undefined | GenericGenObject.GenesysGenUitechnique | undefined | GenericGenObject.GenesysGenWcvfxBehaviourLights | undefined | GenericGenObject.GenesysGenGameplayTriggerOutput | undefined | GenericGenObject.GenesysGenUielementMiniMap | undefined | GenericGenObject.GenesysGenUielementBaseRenderingData | undefined | GenericGenObject.GenesysGenGameMode | undefined | GenericGenObject.GenesysGenPhysicalDefinitionRigidBody | undefined | GenericGenObject.GenesysGenBehaviour | undefined | GenericGenObject.GenesysGenRoadBlockDefinition | undefined | GenericGenObject.GenesysGenEventArena | undefined | GenericGenObject.GenesysGenTextStyle | undefined | GenericGenObject.GenesysGenUielementPrototypeShape | undefined | GenericGenObject.GenesysGenScoreViewModelScoreData | undefined | GenericGenObject.GenesysGenRoadBlockLayerItem | undefined | GenericGenObject.GenesysGenGameRank | undefined | GenericGenObject.GenesysGenEnvironmentKeyframeCamera | undefined | GenericGenObject.GenesysGenGamePack | undefined | GenericGenObject.GenesysGenEventTriggerSequenceItem | undefined | GenericGenObject.GenesysGenNitrousEarningGameRule | undefined | GenericGenObject.GenesysGenSnapToWorldBehaviour | undefined | GenericGenObject.GenesysGenEnvironmentKeyframeWeather | undefined | GenericGenObject.GenesysGenNucleusEntitlementTag | undefined | GenericGenObject.GenesysGenThermalVisionModeProperties | undefined | GenericGenObject.GenesysGenFastLaunchWeaponUpgrade | undefined | GenericGenObject.GenesysGenWeaponUpgrade | undefined | GenericGenObject.GenesysGenScoringAction | undefined | GenericGenObject.GenesysGenEnvironmentKeyframeMiniDof | undefined | GenericGenObject.GenesysGenDustStormMinimapUpgrade | undefined | GenericGenObject.GenesysGenWeapon | undefined | GenericGenObject.GenesysGenUilayoutInstanceParamsTimelineParameters | undefined | GenericGenObject.GenesysGenWcsequenceBehaviour | undefined | GenericGenObject.GenesysGenWcvfxBehaviour | undefined | GenericGenObject.StringBase | undefined | GenericGenObject.GenesysGenRoadblockInstance | undefined | GenericGenObject.GenesysGenSpikeStripWeapon | undefined | GenericGenObject.RwMathVpuVector4 | undefined | GenericGenObject.GenesysGenUielementElementStackTemplate | undefined | GenericGenObject.GenesysGenMakePhysicalBehaviour | undefined | GenericGenObject.RwMathVpuVector3 | undefined | GenericGenObject.GenesysGenPostFxstateColourCubeSettings | undefined | GenericGenObject.GenesysGenUielementMoviePlayer | undefined | GenericGenObject.GenesysGenLightBase | undefined | GenericGenObject.GenesysGenUielementMoviePlayerDimensions | undefined | GenericGenObject.GenesysGenSpeedbreakerWeapon | undefined | GenericGenObject.GenesysGenEnvironmentTimelineTimelineKeyframe | undefined | GenericGenObject.GenesysGenUilayoutInstanceParams | undefined | GenericGenObject.GenesysGenUielementBaseBehaviour | undefined | GenericGenObject.GenesysGenPostFxKeyframeDepthOfField | undefined | GenericGenObject.GenesysGenPhysicalDefinitionRigidBodyBoxVolume | undefined | GenericGenObject.GenesysGenLayoutSequenceItem | undefined | GenericGenObject.RwMathVpuMatrix44affine | undefined | GenericGenObject.GenesysGenUielementBaseTimelineBehaviour | undefined | GenericGenObject.GenesysGenUilayoutInstanceParamsTransformComponents | undefined | GenericGenObject.GenesysGenExtraAmmoWeaponUpgrade | undefined | GenericGenObject.GenesysGenUielementScrollableLabelString | undefined | GenericGenObject.GenesysGenPostFxKeyframe | undefined | GenericGenObject.GenesysGenEnvironmentKeyframeHeatHaze | undefined | GenericGenObject.GenesysGenSetVisionModeTypeSequenceItem | undefined | GenericGenObject.RwRgba | undefined | GenericGenObject.GenesysGenPerformanceUpgradePackage | undefined | GenericGenObject.GenesysGenWeaponRechargeData | undefined | GenericGenObject.GenesysGenBusMixerChannelSequenceItemBusMixerChannelDoubleValue | undefined | GenericGenObject.GenesysGenUielementPrototypeScrollingTextTextProperties | undefined | GenericGenObject.GenesysObjCollection | undefined | GenericGenObject.GenesysGenSequenceTimelineController | undefined | GenericGenObject.GenesysGenCustomChevron | undefined | GenericGenObject.GenesysGenPostFxsequenceItem | undefined | GenericGenObject.GenesysGenImpactDamageGameRule | undefined | GenericGenObject.GenesysGenAddBehaviourSequenceItem | undefined | GenericGenObject.GenesysGenPhysicalDefinitionRigidBodySphereVolume | undefined | GenericGenObject.GenesysGenMixingGroup | undefined | GenericGenObject.RwMathVpuVector2 | undefined | GenericGenObject.GenesysGenRollout | undefined | GenericGenObject.GenesysGenFlashHeadlightsWeapon | undefined | GenericGenObject.GenesysGenGameUnlockMilestone | undefined | GenericGenObject.GenesysGenMixerChannelPriority | undefined | GenericGenObject.GenesysGenWcplaySoundBehaviour | undefined | GenericGenObject.GenesysGenUilayout | undefined | GenericGenObject.GenesysGenCoronaGlow | undefined | GenericGenObject.GenesysGenEventLocation | undefined | GenericGenObject.GenesysGenHypoxParticlesWeaponUpgrade | undefined | GenericGenObject.GenesysGenUielementScrollableLabelTextProperties | undefined | GenericGenObject.GenesysGenPostFxKeyframeBloom | undefined | GenericGenObject.GenesysGenHudStyleSequenceItem | undefined | GenericGenObject.GenesysGenPhysicalExplosionRaceCarInAirExplosion | undefined | GenericGenObject.GenesysGenCarSelectData | undefined | GenericGenObject.GenesysGenUielementPrototypeImageTintProperties | undefined | GenericGenObject.GenesysGenVisionMode | undefined | GenericGenObject.GenesysGenUicamera | undefined | GenericGenObject.GenesysGenCameraGameplayShakeEffect | undefined | GenericGenObject.GenesysGenGameplayTriggerInput | undefined | GenericGenObject.GenesysGenWcvfxBehaviourSpotEffects | undefined | GenericGenObject.GenesysGenWaveSequenceItem | undefined | GenericGenObject.GenesysGenAiplayerInstance | undefined | GenericGenObject.GenesysGenUielementBaseTimeline | undefined | GenericGenObject.GenesysGenEnvironmentTimelineSequenceItem | undefined | GenericGenObject.GenesysGenFlashBangWeapon | undefined | GenericGenObject.GenesysGenGrenadeWeapon | undefined | GenericGenObject.GenesysGenApplyVehicleKickSequenceItem | undefined | GenericGenObject.GenesysGenSmokeScreenWeapon | undefined | GenericGenObject.GenesysGenChevron | undefined | GenericGenObject.GenesysGenPhysicsSequenceItem | undefined | GenericGenObject.GenesysGenImpactProtectionGameRule | undefined | GenericGenObject.GenesysGenCoronaEnvMapGlow | undefined | GenericGenObject.GenesysGenUielementMainMap | undefined | GenericGenObject.GenesysGenCameraGameplayShakeEffectTranslationAxisParams | undefined | GenericGenObject.GenesysGenEvent | undefined | GenericGenObject.GenesysGenUpgradePackage | undefined | GenericGenObject.GenesysGenSoundDistanceFalloff | undefined | GenericGenObject.GenesysGenMineWeapon | undefined | GenericGenObject.GenesysGenUielementBaseEffectConstant | undefined | GenericGenObject.GenesysGenGameUnlock | undefined | GenericGenObject.GenesysGenWcpathAnimationBehaviourAnimationPath | undefined | GenericGenObject.GenesysGenThankYouScreenItem | undefined | GenericGenObject.GenesysGenOnlineEvent | undefined | GenericGenObject.GenesysGenLightPoint | undefined | GenericGenObject.GenesysGenStorePackList | undefined | GenericGenObject.GenesysGenCameraGameplayShakeEffectRotation | undefined | GenericGenObject.GenesysGenPostFxstateValueModifier | undefined | GenericGenObject.GenesysGenPostFxKeyframeVignette | undefined | GenericGenObject.GenesysGenSpikeStripBodyBlowUpgrade | undefined | undefined {
    if (typeof this._data !== 'undefined')
      return this._data;
    let _pos = this._io.pos;
    this._io.seek((this.ofs as any));
    switch ((this.obj as any).muTypeVersion) {
      case 1150238934: {
        this._data = (new GenericGenObject.GenesysGenEnvironmentKeyframeVfx(this._io, this, this._root)) as any
        break;
      }
      case 738476701: {
        this._data = (new GenericGenObject.GenesysGenGameUnlockList(this._io, this, this._root)) as any
        break;
      }
      case 1848619037: {
        this._data = (new GenericGenObject.GenesysGenGameplayMilestoneEntry(this._io, this, this._root)) as any
        break;
      }
      case 379456317: {
        this._data = (new GenericGenObject.GenesysGenTextStyleTextStyleLocale(this._io, this, this._root)) as any
        break;
      }
      case 838894301: {
        this._data = (new GenericGenObject.GenesysGenPerk(this._io, this, this._root)) as any
        break;
      }
      case 2209408025: {
        this._data = (new GenericGenObject.GenesysGenGameplayMilestone(this._io, this, this._root)) as any
        break;
      }
      case 3678829457: {
        this._data = (new GenericGenObject.GenesysGenVfxSpotEffectSequenceItem(this._io, this, this._root)) as any
        break;
      }
      case 2286540362: {
        this._data = (new GenericGenObject.GenesysGenHeatLevel(this._io, this, this._root)) as any
        break;
      }
      case 3128949721: {
        this._data = (new GenericGenObject.GenesysGenUielementPrototypeImage(this._io, this, this._root)) as any
        break;
      }
      case 1668851487: {
        this._data = (new GenericGenObject.GenesysGenCarSelectDataSequences(this._io, this, this._root)) as any
        break;
      }
      case 3657730227: {
        this._data = (new GenericGenObject.GenesysGenUielementPrototypeLabel(this._io, this, this._root)) as any
        break;
      }
      case 1566205417: {
        this._data = (new GenericGenObject.GenesysGenWchideBehaviour(this._io, this, this._root)) as any
        break;
      }
      case 1840158847: {
        this._data = (new GenericGenObject.GenesysGenPerkLevel(this._io, this, this._root)) as any
        break;
      }
      case 3174528889: {
        this._data = (new GenericGenObject.GenesysGenGameplayTriggerOutputSequenceOutput(this._io, this, this._root)) as any
        break;
      }
      case 1671215869: {
        this._data = (new GenericGenObject.GenesysGenThankyouMapping(this._io, this, this._root)) as any
        break;
      }
      case 981367156: {
        this._data = (new GenericGenObject.GenesysGenEventList(this._io, this, this._root)) as any
        break;
      }
      case 2947788458: {
        this._data = (new GenericGenObject.GenesysGenStoreItem(this._io, this, this._root)) as any
        break;
      }
      case 3989427985: {
        this._data = (new GenericGenObject.GenesysGenLightCone(this._io, this, this._root)) as any
        break;
      }
      case 2560361681: {
        this._data = (new GenericGenObject.GenesysGenEntitlement(this._io, this, this._root)) as any
        break;
      }
      case 1859689840: {
        this._data = (new GenericGenObject.GenesysGenTeflonSlickWeapon(this._io, this, this._root)) as any
        break;
      }
      case 2446666186: {
        this._data = (new GenericGenObject.GenesysGenEnvironmentTimeline(this._io, this, this._root)) as any
        break;
      }
      case 41223923: {
        this._data = (new GenericGenObject.GenesysGenSpikeStripBlowoutUpgrade(this._io, this, this._root)) as any
        break;
      }
      case 1694754426: {
        this._data = (new GenericGenObject.GenesysGenRoadBlockLayer(this._io, this, this._root)) as any
        break;
      }
      case 2442478334: {
        this._data = (new GenericGenObject.GenesysGenPhysicalExplosionGameplayExplosion(this._io, this, this._root)) as any
        break;
      }
      case 4075515997: {
        this._data = (new GenericGenObject.GenesysGenUielementElementStack(this._io, this, this._root)) as any
        break;
      }
      case 2353481207: {
        this._data = (new GenericGenObject.GenesysGenEnvironmentKeyframe(this._io, this, this._root)) as any
        break;
      }
      case 4092156414: {
        this._data = (new GenericGenObject.GenesysGenArcLightConeUpgrade(this._io, this, this._root)) as any
        break;
      }
      case 3067799153: {
        this._data = (new GenericGenObject.GenesysGenSequenceItemModulatingDoubleValue(this._io, this, this._root)) as any
        break;
      }
      case 2152868223: {
        this._data = (new GenericGenObject.GenesysGenAiplayerType(this._io, this, this._root)) as any
        break;
      }
      case 1766412136: {
        this._data = (new GenericGenObject.GenesysGenSequenceItem(this._io, this, this._root)) as any
        break;
      }
      case 115778840: {
        this._data = (new GenericGenObject.GenesysGenJumpTimelineController(this._io, this, this._root)) as any
        break;
      }
      case 606894659: {
        this._data = (new GenericGenObject.GenesysGenGameplayTrigger(this._io, this, this._root)) as any
        break;
      }
      case 3071320584: {
        this._data = (new GenericGenObject.GenesysGenStorePack(this._io, this, this._root)) as any
        break;
      }
      case 306714612: {
        this._data = (new GenericGenObject.GenesysGenLightBaseFlashPattern(this._io, this, this._root)) as any
        break;
      }
      case 2462007859: {
        this._data = (new GenericGenObject.GenesysGenPhysicalDefinition(this._io, this, this._root)) as any
        break;
      }
      case 2048015465: {
        this._data = (new GenericGenObject.GenesysGenHeatLevelCopType(this._io, this, this._root)) as any
        break;
      }
      case 4243611625: {
        this._data = (new GenericGenObject.GenesysGenSequence(this._io, this, this._root)) as any
        break;
      }
      case 3513065817: {
        this._data = (new GenericGenObject.GenesysGenBusMixerChannelSequenceItem(this._io, this, this._root)) as any
        break;
      }
      case 3784314544: {
        this._data = (new GenericGenObject.GenesysGenUielementBase(this._io, this, this._root)) as any
        break;
      }
      case 1375788276: {
        this._data = (new GenericGenObject.GenesysGenGameUnlockEvent(this._io, this, this._root)) as any
        break;
      }
      case 2290736886: {
        this._data = (new GenericGenObject.GenesysGenAnimationSequenceItem(this._io, this, this._root)) as any
        break;
      }
      case 1701879475: {
        this._data = (new GenericGenObject.GenesysGenWeaponList(this._io, this, this._root)) as any
        break;
      }
      case 3685969725: {
        this._data = (new GenericGenObject.GenesysGenUielementPrototypeScrollingTextString(this._io, this, this._root)) as any
        break;
      }
      case 3652314633: {
        this._data = (new GenericGenObject.GenesysGenCameraGameplayShakeEffectRotationAxisParams(this._io, this, this._root)) as any
        break;
      }
      case 503737009: {
        this._data = (new GenericGenObject.GenesysGenOfflineEvent(this._io, this, this._root)) as any
        break;
      }
      case 3763436769: {
        this._data = (new GenericGenObject.GenesysGenGameModeScoreOverride(this._io, this, this._root)) as any
        break;
      }
      case 615742248: {
        this._data = (new GenericGenObject.GenesysGenPostFxstate(this._io, this, this._root)) as any
        break;
      }
      case 1819824028: {
        this._data = (new GenericGenObject.GenesysGenPhysicalExplosion(this._io, this, this._root)) as any
        break;
      }
      case 3046792924: {
        this._data = (new GenericGenObject.GenesysGenCoronaBeam(this._io, this, this._root)) as any
        break;
      }
      case 1284749351: {
        this._data = (new GenericGenObject.GenesysGenSilentLaunchWeaponUpgrade(this._io, this, this._root)) as any
        break;
      }
      case 1856748625: {
        this._data = (new GenericGenObject.GenesysGenUielementScrollableLabel(this._io, this, this._root)) as any
        break;
      }
      case 930210423: {
        this._data = (new GenericGenObject.GenesysGenPhysicalExplosionNonRaceCarExplosion(this._io, this, this._root)) as any
        break;
      }
      case 2027355840: {
        this._data = (new GenericGenObject.GenesysGenUimaterial(this._io, this, this._root)) as any
        break;
      }
      case 1324301512: {
        this._data = (new GenericGenObject.GenesysGenPostFxKeyframeStereo3d(this._io, this, this._root)) as any
        break;
      }
      case 2470623620: {
        this._data = (new GenericGenObject.GenesysGenSlowMoSequenceItem(this._io, this, this._root)) as any
        break;
      }
      case 4085824509: {
        this._data = (new GenericGenObject.GenesysGenPostFxKeyframeGeneral(this._io, this, this._root)) as any
        break;
      }
      case 3956246192: {
        this._data = (new GenericGenObject.GenesysGenPhysicsSequenceItemPhysicsDoubleValue(this._io, this, this._root)) as any
        break;
      }
      case 1562403887: {
        this._data = (new GenericGenObject.GenesysGenUielementPrototypeImageOpacity(this._io, this, this._root)) as any
        break;
      }
      case 536982309: {
        this._data = (new GenericGenObject.GenesysGenWcpathAnimationBehaviour(this._io, this, this._root)) as any
        break;
      }
      case 619283814: {
        this._data = (new GenericGenObject.GenesysGenUielementMask(this._io, this, this._root)) as any
        break;
      }
      case 1683395683: {
        this._data = (new GenericGenObject.GenesysGenEnvironmentKeyframeLightRig(this._io, this, this._root)) as any
        break;
      }
      case 2321694493: {
        this._data = (new GenericGenObject.GenesysGenWaveSequenceItemFade(this._io, this, this._root)) as any
        break;
      }
      case 866205257: {
        this._data = (new GenericGenObject.GenesysGenCameraGameplayShakeEffectTranslation(this._io, this, this._root)) as any
        break;
      }
      case 18021398: {
        this._data = (new GenericGenObject.GenesysGenPhysicalDefinitionRigidBodyCylinderVolume(this._io, this, this._root)) as any
        break;
      }
      case 3798955972: {
        this._data = (new GenericGenObject.GenesysGenUielementPrototypeLabelString(this._io, this, this._root)) as any
        break;
      }
      case 1557152310: {
        this._data = (new GenericGenObject.GenesysGenCameraShakeSequenceItem(this._io, this, this._root)) as any
        break;
      }
      case 2935374172: {
        this._data = (new GenericGenObject.GenesysGenEventArenaData(this._io, this, this._root)) as any
        break;
      }
      case 4162446969: {
        this._data = (new GenericGenObject.GenesysGenCorona(this._io, this, this._root)) as any
        break;
      }
      case 3549903212: {
        this._data = (new GenericGenObject.GenesysGenScoreViewModel(this._io, this, this._root)) as any
        break;
      }
      case 3309031391: {
        this._data = (new GenericGenObject.GenesysGenJammerWeapon(this._io, this, this._root)) as any
        break;
      }
      case 1304174185: {
        this._data = (new GenericGenObject.GenesysGenThermalVisionMode(this._io, this, this._root)) as any
        break;
      }
      case 4263309034: {
        this._data = (new GenericGenObject.GenesysGenNucleusGrantMappingsListMapping(this._io, this, this._root)) as any
        break;
      }
      case 3756202357: {
        this._data = (new GenericGenObject.GenesysGenWcvfxBehaviourCoronas(this._io, this, this._root)) as any
        break;
      }
      case 275461846: {
        this._data = (new GenericGenObject.GenesysGenEnvironmentKeyframeClouds(this._io, this, this._root)) as any
        break;
      }
      case 3131401224: {
        this._data = (new GenericGenObject.GenesysGenNucleusEntitlementTags(this._io, this, this._root)) as any
        break;
      }
      case 1664340785: {
        this._data = (new GenericGenObject.GenesysGenPhysicalDefinitionRigidBodyConvexHullVolume(this._io, this, this._root)) as any
        break;
      }
      case 494037508: {
        this._data = (new GenericGenObject.GenesysGenGameRule(this._io, this, this._root)) as any
        break;
      }
      case 3718953067: {
        this._data = (new GenericGenObject.GenesysGenMixerChannel(this._io, this, this._root)) as any
        break;
      }
      case 3115085927: {
        this._data = (new GenericGenObject.GenesysGenWcplaySoundBehaviourPropSurfaceSound(this._io, this, this._root)) as any
        break;
      }
      case 790547232: {
        this._data = (new GenericGenObject.GenesysGenEnvironmentKeyframeFog(this._io, this, this._root)) as any
        break;
      }
      case 3285476138: {
        this._data = (new GenericGenObject.GenesysGenUielementPrototypeLabelTextProperties(this._io, this, this._root)) as any
        break;
      }
      case 4248992647: {
        this._data = (new GenericGenObject.GenesysGenDeviceGrantUpgradePackage(this._io, this, this._root)) as any
        break;
      }
      case 3502480523: {
        this._data = (new GenericGenObject.GenesysGenNitrousBurningGameRule(this._io, this, this._root)) as any
        break;
      }
      case 1055028229: {
        this._data = (new GenericGenObject.GenesysGenWcremoveWorldEntityBehaviour(this._io, this, this._root)) as any
        break;
      }
      case 3431394552: {
        this._data = (new GenericGenObject.GenesysGenUielementPrototypeScrollingText(this._io, this, this._root)) as any
        break;
      }
      case 3314905645: {
        this._data = (new GenericGenObject.GenesysGenPhysicalExplosionRaceCarOnGroundExplosion(this._io, this, this._root)) as any
        break;
      }
      case 3340139760: {
        this._data = (new GenericGenObject.GenesysGenHelicopterWeapon(this._io, this, this._root)) as any
        break;
      }
      case 3386454351: {
        this._data = (new GenericGenObject.GenesysGenRolloutWeaponData(this._io, this, this._root)) as any
        break;
      }
      case 975568910: {
        this._data = (new GenericGenObject.GenesysGenNucleusGrantMappingsList(this._io, this, this._root)) as any
        break;
      }
      case 2557796749: {
        this._data = (new GenericGenObject.GenesysGenSearchlightBehaviour(this._io, this, this._root)) as any
        break;
      }
      case 2913275356: {
        this._data = (new GenericGenObject.GenesysGenCoronaFlare(this._io, this, this._root)) as any
        break;
      }
      case 1721661981: {
        this._data = (new GenericGenObject.GenesysGenOfflineEventCustomChevrons(this._io, this, this._root)) as any
        break;
      }
      case 1057898069: {
        this._data = (new GenericGenObject.GenesysGenUicolour(this._io, this, this._root)) as any
        break;
      }
      case 3450467609: {
        this._data = (new GenericGenObject.GenesysGenEnvironmentKeyframeSky(this._io, this, this._root)) as any
        break;
      }
      case 3638622566: {
        this._data = (new GenericGenObject.GenesysGenUitechnique(this._io, this, this._root)) as any
        break;
      }
      case 3417537371: {
        this._data = (new GenericGenObject.GenesysGenWcvfxBehaviourLights(this._io, this, this._root)) as any
        break;
      }
      case 1454972863: {
        this._data = (new GenericGenObject.GenesysGenGameplayTriggerOutput(this._io, this, this._root)) as any
        break;
      }
      case 1705261723: {
        this._data = (new GenericGenObject.GenesysGenUielementMiniMap(this._io, this, this._root)) as any
        break;
      }
      case 4158115530: {
        this._data = (new GenericGenObject.GenesysGenUielementBaseRenderingData(this._io, this, this._root)) as any
        break;
      }
      case 1137921905: {
        this._data = (new GenericGenObject.GenesysGenGameMode(this._io, this, this._root)) as any
        break;
      }
      case 2362053299: {
        this._data = (new GenericGenObject.GenesysGenPhysicalDefinitionRigidBody(this._io, this, this._root)) as any
        break;
      }
      case 160896465: {
        this._data = (new GenericGenObject.GenesysGenBehaviour(this._io, this, this._root)) as any
        break;
      }
      case 2953390990: {
        this._data = (new GenericGenObject.GenesysGenRoadBlockDefinition(this._io, this, this._root)) as any
        break;
      }
      case 2545624958: {
        this._data = (new GenericGenObject.GenesysGenEventArena(this._io, this, this._root)) as any
        break;
      }
      case 2006191741: {
        this._data = (new GenericGenObject.GenesysGenTextStyle(this._io, this, this._root)) as any
        break;
      }
      case 394486533: {
        this._data = (new GenericGenObject.GenesysGenUielementPrototypeShape(this._io, this, this._root)) as any
        break;
      }
      case 606909642: {
        this._data = (new GenericGenObject.GenesysGenScoreViewModelScoreData(this._io, this, this._root)) as any
        break;
      }
      case 2808391399: {
        this._data = (new GenericGenObject.GenesysGenRoadBlockLayerItem(this._io, this, this._root)) as any
        break;
      }
      case 1881019249: {
        this._data = (new GenericGenObject.GenesysGenGameRank(this._io, this, this._root)) as any
        break;
      }
      case 1895175564: {
        this._data = (new GenericGenObject.GenesysGenEnvironmentKeyframeCamera(this._io, this, this._root)) as any
        break;
      }
      case 3562210973: {
        this._data = (new GenericGenObject.GenesysGenGamePack(this._io, this, this._root)) as any
        break;
      }
      case 2519589055: {
        this._data = (new GenericGenObject.GenesysGenEventTriggerSequenceItem(this._io, this, this._root)) as any
        break;
      }
      case 2358324053: {
        this._data = (new GenericGenObject.GenesysGenNitrousEarningGameRule(this._io, this, this._root)) as any
        break;
      }
      case 3877549313: {
        this._data = (new GenericGenObject.GenesysGenSnapToWorldBehaviour(this._io, this, this._root)) as any
        break;
      }
      case 3650553990: {
        this._data = (new GenericGenObject.GenesysGenEnvironmentKeyframeWeather(this._io, this, this._root)) as any
        break;
      }
      case 1212586379: {
        this._data = (new GenericGenObject.GenesysGenNucleusEntitlementTag(this._io, this, this._root)) as any
        break;
      }
      case 2721335456: {
        this._data = (new GenericGenObject.GenesysGenThermalVisionModeProperties(this._io, this, this._root)) as any
        break;
      }
      case 3966750237: {
        this._data = (new GenericGenObject.GenesysGenFastLaunchWeaponUpgrade(this._io, this, this._root)) as any
        break;
      }
      case 887880830: {
        this._data = (new GenericGenObject.GenesysGenWeaponUpgrade(this._io, this, this._root)) as any
        break;
      }
      case 2252967758: {
        this._data = (new GenericGenObject.GenesysGenScoringAction(this._io, this, this._root)) as any
        break;
      }
      case 3750941088: {
        this._data = (new GenericGenObject.GenesysGenEnvironmentKeyframeMiniDof(this._io, this, this._root)) as any
        break;
      }
      case 2327923899: {
        this._data = (new GenericGenObject.GenesysGenDustStormMinimapUpgrade(this._io, this, this._root)) as any
        break;
      }
      case 3688241096: {
        this._data = (new GenericGenObject.GenesysGenWeapon(this._io, this, this._root)) as any
        break;
      }
      case 796059478: {
        this._data = (new GenericGenObject.GenesysGenUilayoutInstanceParamsTimelineParameters(this._io, this, this._root)) as any
        break;
      }
      case 3428371066: {
        this._data = (new GenericGenObject.GenesysGenWcsequenceBehaviour(this._io, this, this._root)) as any
        break;
      }
      case 32647085: {
        this._data = (new GenericGenObject.GenesysGenWcvfxBehaviour(this._io, this, this._root)) as any
        break;
      }
      case 2516314814: {
        this._data = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
        break;
      }
      case 2089690370: {
        this._data = (new GenericGenObject.GenesysGenRoadblockInstance(this._io, this, this._root)) as any
        break;
      }
      case 1589479971: {
        this._data = (new GenericGenObject.GenesysGenSpikeStripWeapon(this._io, this, this._root)) as any
        break;
      }
      case 3257509935: {
        this._data = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
        break;
      }
      case 3175993083: {
        this._data = (new GenericGenObject.GenesysGenUielementElementStackTemplate(this._io, this, this._root)) as any
        break;
      }
      case 477258504: {
        this._data = (new GenericGenObject.GenesysGenMakePhysicalBehaviour(this._io, this, this._root)) as any
        break;
      }
      case 2784336371: {
        this._data = (new GenericGenObject.RwMathVpuVector3(this._io, this, this._root)) as any
        break;
      }
      case 2006186034: {
        this._data = (new GenericGenObject.GenesysGenPostFxstateColourCubeSettings(this._io, this, this._root)) as any
        break;
      }
      case 3864748285: {
        this._data = (new GenericGenObject.GenesysGenUielementMoviePlayer(this._io, this, this._root)) as any
        break;
      }
      case 4046186056: {
        this._data = (new GenericGenObject.GenesysGenLightBase(this._io, this, this._root)) as any
        break;
      }
      case 1386995851: {
        this._data = (new GenericGenObject.GenesysGenUielementMoviePlayerDimensions(this._io, this, this._root)) as any
        break;
      }
      case 3548375797: {
        this._data = (new GenericGenObject.GenesysGenSpeedbreakerWeapon(this._io, this, this._root)) as any
        break;
      }
      case 4341541: {
        this._data = (new GenericGenObject.GenesysGenEnvironmentTimelineTimelineKeyframe(this._io, this, this._root)) as any
        break;
      }
      case 3550644905: {
        this._data = (new GenericGenObject.GenesysGenUilayoutInstanceParams(this._io, this, this._root)) as any
        break;
      }
      case 327168116: {
        this._data = (new GenericGenObject.GenesysGenUielementBaseBehaviour(this._io, this, this._root)) as any
        break;
      }
      case 1600514099: {
        this._data = (new GenericGenObject.GenesysGenPostFxKeyframeDepthOfField(this._io, this, this._root)) as any
        break;
      }
      case 2630734184: {
        this._data = (new GenericGenObject.GenesysGenPhysicalDefinitionRigidBodyBoxVolume(this._io, this, this._root)) as any
        break;
      }
      case 2878684940: {
        this._data = (new GenericGenObject.GenesysGenLayoutSequenceItem(this._io, this, this._root)) as any
        break;
      }
      case 3062587406: {
        this._data = (new GenericGenObject.RwMathVpuMatrix44affine(this._io, this, this._root)) as any
        break;
      }
      case 641453515: {
        this._data = (new GenericGenObject.GenesysGenUielementBaseTimelineBehaviour(this._io, this, this._root)) as any
        break;
      }
      case 1830374425: {
        this._data = (new GenericGenObject.GenesysGenUilayoutInstanceParamsTransformComponents(this._io, this, this._root)) as any
        break;
      }
      case 1658948550: {
        this._data = (new GenericGenObject.GenesysGenExtraAmmoWeaponUpgrade(this._io, this, this._root)) as any
        break;
      }
      case 504799179: {
        this._data = (new GenericGenObject.GenesysGenUielementScrollableLabelString(this._io, this, this._root)) as any
        break;
      }
      case 1519651292: {
        this._data = (new GenericGenObject.GenesysGenPostFxKeyframe(this._io, this, this._root)) as any
        break;
      }
      case 4259325714: {
        this._data = (new GenericGenObject.GenesysGenEnvironmentKeyframeHeatHaze(this._io, this, this._root)) as any
        break;
      }
      case 1583304527: {
        this._data = (new GenericGenObject.GenesysGenSetVisionModeTypeSequenceItem(this._io, this, this._root)) as any
        break;
      }
      case 185604263: {
        this._data = (new GenericGenObject.RwRgba(this._io, this, this._root)) as any
        break;
      }
      case 546410997: {
        this._data = (new GenericGenObject.GenesysGenPerformanceUpgradePackage(this._io, this, this._root)) as any
        break;
      }
      case 3688569486: {
        this._data = (new GenericGenObject.GenesysGenWeaponRechargeData(this._io, this, this._root)) as any
        break;
      }
      case 41209892: {
        this._data = (new GenericGenObject.GenesysGenBusMixerChannelSequenceItemBusMixerChannelDoubleValue(this._io, this, this._root)) as any
        break;
      }
      case 4168741296: {
        this._data = (new GenericGenObject.GenesysGenUielementPrototypeScrollingTextTextProperties(this._io, this, this._root)) as any
        break;
      }
      case 3162856831: {
        this._data = (new GenericGenObject.GenesysObjCollection(this._io, this, this._root)) as any
        break;
      }
      case 4067794056: {
        this._data = (new GenericGenObject.GenesysGenSequenceTimelineController(this._io, this, this._root)) as any
        break;
      }
      case 2896762174: {
        this._data = (new GenericGenObject.GenesysGenCustomChevron(this._io, this, this._root)) as any
        break;
      }
      case 2580244534: {
        this._data = (new GenericGenObject.GenesysGenPostFxsequenceItem(this._io, this, this._root)) as any
        break;
      }
      case 437108292: {
        this._data = (new GenericGenObject.GenesysGenImpactDamageGameRule(this._io, this, this._root)) as any
        break;
      }
      case 4281548263: {
        this._data = (new GenericGenObject.GenesysGenAddBehaviourSequenceItem(this._io, this, this._root)) as any
        break;
      }
      case 4179189423: {
        this._data = (new GenericGenObject.GenesysGenPhysicalDefinitionRigidBodySphereVolume(this._io, this, this._root)) as any
        break;
      }
      case 4049496118: {
        this._data = (new GenericGenObject.GenesysGenMixingGroup(this._io, this, this._root)) as any
        break;
      }
      case 786918963: {
        this._data = (new GenericGenObject.RwMathVpuVector2(this._io, this, this._root)) as any
        break;
      }
      case 3685564593: {
        this._data = (new GenericGenObject.GenesysGenRollout(this._io, this, this._root)) as any
        break;
      }
      case 3376466135: {
        this._data = (new GenericGenObject.GenesysGenFlashHeadlightsWeapon(this._io, this, this._root)) as any
        break;
      }
      case 1216293293: {
        this._data = (new GenericGenObject.GenesysGenGameUnlockMilestone(this._io, this, this._root)) as any
        break;
      }
      case 2235129779: {
        this._data = (new GenericGenObject.GenesysGenMixerChannelPriority(this._io, this, this._root)) as any
        break;
      }
      case 4218582003: {
        this._data = (new GenericGenObject.GenesysGenWcplaySoundBehaviour(this._io, this, this._root)) as any
        break;
      }
      case 2792624488: {
        this._data = (new GenericGenObject.GenesysGenUilayout(this._io, this, this._root)) as any
        break;
      }
      case 3106938524: {
        this._data = (new GenericGenObject.GenesysGenCoronaGlow(this._io, this, this._root)) as any
        break;
      }
      case 3916132985: {
        this._data = (new GenericGenObject.GenesysGenEventLocation(this._io, this, this._root)) as any
        break;
      }
      case 3895972908: {
        this._data = (new GenericGenObject.GenesysGenHypoxParticlesWeaponUpgrade(this._io, this, this._root)) as any
        break;
      }
      case 1094276132: {
        this._data = (new GenericGenObject.GenesysGenUielementScrollableLabelTextProperties(this._io, this, this._root)) as any
        break;
      }
      case 3592057837: {
        this._data = (new GenericGenObject.GenesysGenPostFxKeyframeBloom(this._io, this, this._root)) as any
        break;
      }
      case 137884438: {
        this._data = (new GenericGenObject.GenesysGenHudStyleSequenceItem(this._io, this, this._root)) as any
        break;
      }
      case 2027177213: {
        this._data = (new GenericGenObject.GenesysGenPhysicalExplosionRaceCarInAirExplosion(this._io, this, this._root)) as any
        break;
      }
      case 4000545794: {
        this._data = (new GenericGenObject.GenesysGenCarSelectData(this._io, this, this._root)) as any
        break;
      }
      case 1079751127: {
        this._data = (new GenericGenObject.GenesysGenUielementPrototypeImageTintProperties(this._io, this, this._root)) as any
        break;
      }
      case 2653977028: {
        this._data = (new GenericGenObject.GenesysGenVisionMode(this._io, this, this._root)) as any
        break;
      }
      case 4265727012: {
        this._data = (new GenericGenObject.GenesysGenUicamera(this._io, this, this._root)) as any
        break;
      }
      case 3580468080: {
        this._data = (new GenericGenObject.GenesysGenCameraGameplayShakeEffect(this._io, this, this._root)) as any
        break;
      }
      case 934085957: {
        this._data = (new GenericGenObject.GenesysGenGameplayTriggerInput(this._io, this, this._root)) as any
        break;
      }
      case 3960909674: {
        this._data = (new GenericGenObject.GenesysGenWcvfxBehaviourSpotEffects(this._io, this, this._root)) as any
        break;
      }
      case 897852783: {
        this._data = (new GenericGenObject.GenesysGenWaveSequenceItem(this._io, this, this._root)) as any
        break;
      }
      case 2775196711: {
        this._data = (new GenericGenObject.GenesysGenAiplayerInstance(this._io, this, this._root)) as any
        break;
      }
      case 2925930439: {
        this._data = (new GenericGenObject.GenesysGenUielementBaseTimeline(this._io, this, this._root)) as any
        break;
      }
      case 2293547115: {
        this._data = (new GenericGenObject.GenesysGenEnvironmentTimelineSequenceItem(this._io, this, this._root)) as any
        break;
      }
      case 2222312579: {
        this._data = (new GenericGenObject.GenesysGenFlashBangWeapon(this._io, this, this._root)) as any
        break;
      }
      case 2687264588: {
        this._data = (new GenericGenObject.GenesysGenGrenadeWeapon(this._io, this, this._root)) as any
        break;
      }
      case 3096674344: {
        this._data = (new GenericGenObject.GenesysGenApplyVehicleKickSequenceItem(this._io, this, this._root)) as any
        break;
      }
      case 3302600098: {
        this._data = (new GenericGenObject.GenesysGenSmokeScreenWeapon(this._io, this, this._root)) as any
        break;
      }
      case 850192155: {
        this._data = (new GenericGenObject.GenesysGenChevron(this._io, this, this._root)) as any
        break;
      }
      case 1542147887: {
        this._data = (new GenericGenObject.GenesysGenPhysicsSequenceItem(this._io, this, this._root)) as any
        break;
      }
      case 3993684758: {
        this._data = (new GenericGenObject.GenesysGenImpactProtectionGameRule(this._io, this, this._root)) as any
        break;
      }
      case 2729521159: {
        this._data = (new GenericGenObject.GenesysGenCoronaEnvMapGlow(this._io, this, this._root)) as any
        break;
      }
      case 2199276125: {
        this._data = (new GenericGenObject.GenesysGenUielementMainMap(this._io, this, this._root)) as any
        break;
      }
      case 3529693283: {
        this._data = (new GenericGenObject.GenesysGenCameraGameplayShakeEffectTranslationAxisParams(this._io, this, this._root)) as any
        break;
      }
      case 1762060451: {
        this._data = (new GenericGenObject.GenesysGenEvent(this._io, this, this._root)) as any
        break;
      }
      case 3632275044: {
        this._data = (new GenericGenObject.GenesysGenUpgradePackage(this._io, this, this._root)) as any
        break;
      }
      case 174014684: {
        this._data = (new GenericGenObject.GenesysGenSoundDistanceFalloff(this._io, this, this._root)) as any
        break;
      }
      case 1363031339: {
        this._data = (new GenericGenObject.GenesysGenMineWeapon(this._io, this, this._root)) as any
        break;
      }
      case 1862050451: {
        this._data = (new GenericGenObject.GenesysGenUielementBaseEffectConstant(this._io, this, this._root)) as any
        break;
      }
      case 2537571270: {
        this._data = (new GenericGenObject.GenesysGenGameUnlock(this._io, this, this._root)) as any
        break;
      }
      case 4150677881: {
        this._data = (new GenericGenObject.GenesysGenWcpathAnimationBehaviourAnimationPath(this._io, this, this._root)) as any
        break;
      }
      case 2578912561: {
        this._data = (new GenericGenObject.GenesysGenThankYouScreenItem(this._io, this, this._root)) as any
        break;
      }
      case 2711283431: {
        this._data = (new GenericGenObject.GenesysGenOnlineEvent(this._io, this, this._root)) as any
        break;
      }
      case 3975851796: {
        this._data = (new GenericGenObject.GenesysGenLightPoint(this._io, this, this._root)) as any
        break;
      }
      case 3573113074: {
        this._data = (new GenericGenObject.GenesysGenStorePackList(this._io, this, this._root)) as any
        break;
      }
      case 1220037810: {
        this._data = (new GenericGenObject.GenesysGenCameraGameplayShakeEffectRotation(this._io, this, this._root)) as any
        break;
      }
      case 4120564202: {
        this._data = (new GenericGenObject.GenesysGenPostFxstateValueModifier(this._io, this, this._root)) as any
        break;
      }
      case 3180273648: {
        this._data = (new GenericGenObject.GenesysGenPostFxKeyframeVignette(this._io, this, this._root)) as any
        break;
      }
      case 1441812963: {
        this._data = (new GenericGenObject.GenesysGenSpikeStripBodyBlowUpgrade(this._io, this, this._root)) as any
        break;
      }
    }
    this._io.seek(_pos);
    return this._data;
  }

  saveOfs: Uint8Array | undefined;
  obj: GenericGenObject.GenObj;
}

export namespace GenericGenObject {
  export class GenesysGenCorona {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.arrInlineFloat32T0xc = [];
      for (let i = 0; i < 6; i++) {
        this.arrInlineFloat32T0xc.push(this._io.readF4be());
      }
      this.arrInlineFloat32T0x24 = [];
      for (let i = 0; i < 6; i++) {
        this.arrInlineFloat32T0x24.push(this._io.readF4be());
      }
      this.arrInlineFloat32T0x3c = [];
      for (let i = 0; i < 6; i++) {
        this.arrInlineFloat32T0x3c.push(this._io.readF4be());
      }
      this.gameChangerId0x54 = (this._io.readU4be()) as any
      this.maxVisibleDistance0x58 = (this._io.readF4be()) as any
      this.visibilityTestDepthBias0x5c = (this._io.readF4be()) as any
      this.ptrArrBeams0x60 = (this._io.readU4be()) as any
      this.ptrArrFlares0x64 = (this._io.readU4be()) as any
      this.ptrArrEnvMapGlows0x68 = (this._io.readU4be()) as any
      this.ptrArrGlows0x6c = (this._io.readU4be()) as any
      this.ptrArrPlanarReflectionGlows0x70 = (this._io.readU4be()) as any
      this.ptrArrRearViewMirrorGlows0x74 = (this._io.readU4be()) as any
      this.arrayCountFor0x60 = (this._io.readU2be()) as any
      this.arrayCountFor0x68 = (this._io.readU2be()) as any
      this.arrayCountFor0x64 = (this._io.readU2be()) as any
      this.arrayCountFor0x6c = (this._io.readU2be()) as any
      this.arrayCountFor0xc = (this._io.readU2be()) as any
      this.arrayCountFor0x24 = (this._io.readU2be()) as any
      this.arrayCountFor0x70 = (this._io.readU2be()) as any
      this.arrayCountFor0x74 = (this._io.readU2be()) as any
      this.arrayCountFor0x3c = (this._io.readU2be()) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _instGlows0x6c: Array<number | undefined> | undefined;
    get instGlows0x6c(): Array<number | undefined> | undefined {
      if (typeof this._instGlows0x6c !== 'undefined')
        return this._instGlows0x6c;
      if ((this.ptrArrGlows0x6c as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrGlows0x6c as any));
        this._instGlows0x6c = [];
        for (let i = 0; i < (this.arrayCountFor0x6c as any); i++) {
          this._instGlows0x6c.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._instGlows0x6c;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (140) as any
      return this._size;
    }

    private _instRearViewMirrorGlows0x74: Array<number | undefined> | undefined;
    get instRearViewMirrorGlows0x74(): Array<number | undefined> | undefined {
      if (typeof this._instRearViewMirrorGlows0x74 !== 'undefined')
        return this._instRearViewMirrorGlows0x74;
      if ((this.ptrArrRearViewMirrorGlows0x74 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrRearViewMirrorGlows0x74 as any));
        this._instRearViewMirrorGlows0x74 = [];
        for (let i = 0; i < (this.arrayCountFor0x74 as any); i++) {
          this._instRearViewMirrorGlows0x74.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._instRearViewMirrorGlows0x74;
    }

    private _instFlares0x64: Array<number | undefined> | undefined;
    get instFlares0x64(): Array<number | undefined> | undefined {
      if (typeof this._instFlares0x64 !== 'undefined')
        return this._instFlares0x64;
      if ((this.ptrArrFlares0x64 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrFlares0x64 as any));
        this._instFlares0x64 = [];
        for (let i = 0; i < (this.arrayCountFor0x64 as any); i++) {
          this._instFlares0x64.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._instFlares0x64;
    }

    private _instEnvMapGlows0x68: Array<number | undefined> | undefined;
    get instEnvMapGlows0x68(): Array<number | undefined> | undefined {
      if (typeof this._instEnvMapGlows0x68 !== 'undefined')
        return this._instEnvMapGlows0x68;
      if ((this.ptrArrEnvMapGlows0x68 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrEnvMapGlows0x68 as any));
        this._instEnvMapGlows0x68 = [];
        for (let i = 0; i < (this.arrayCountFor0x68 as any); i++) {
          this._instEnvMapGlows0x68.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._instEnvMapGlows0x68;
    }

    private _instBeams0x60: Array<number | undefined> | undefined;
    get instBeams0x60(): Array<number | undefined> | undefined {
      if (typeof this._instBeams0x60 !== 'undefined')
        return this._instBeams0x60;
      if ((this.ptrArrBeams0x60 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrBeams0x60 as any));
        this._instBeams0x60 = [];
        for (let i = 0; i < (this.arrayCountFor0x60 as any); i++) {
          this._instBeams0x60.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._instBeams0x60;
    }

    private _instPlanarReflectionGlows0x70: Array<number | undefined> | undefined;
    get instPlanarReflectionGlows0x70(): Array<number | undefined> | undefined {
      if (typeof this._instPlanarReflectionGlows0x70 !== 'undefined')
        return this._instPlanarReflectionGlows0x70;
      if ((this.ptrArrPlanarReflectionGlows0x70 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrPlanarReflectionGlows0x70 as any));
        this._instPlanarReflectionGlows0x70 = [];
        for (let i = 0; i < (this.arrayCountFor0x70 as any); i++) {
          this._instPlanarReflectionGlows0x70.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._instPlanarReflectionGlows0x70;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (4162446969) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    arrInlineFloat32T0xc: Array<number>;
    arrInlineFloat32T0x24: Array<number>;
    arrInlineFloat32T0x3c: Array<number>;
    gameChangerId0x54: number;
    maxVisibleDistance0x58: number;
    visibilityTestDepthBias0x5c: number;

    /**
     * enum; 00_00_32_93_1
     */
    ptrArrBeams0x60: number;

    /**
     * enum; 00_00_32_94_1
     */
    ptrArrFlares0x64: number;

    /**
     * enum; 00_00_32_91_1
     */
    ptrArrEnvMapGlows0x68: number;

    /**
     * enum; 00_00_32_91_1
     */
    ptrArrGlows0x6c: number;

    /**
     * enum; 00_00_32_91_1
     */
    ptrArrPlanarReflectionGlows0x70: number;

    /**
     * enum; 00_00_32_91_1
     */
    ptrArrRearViewMirrorGlows0x74: number;

    /**
     * "BeamsCount"
     */
    arrayCountFor0x60: number;

    /**
     * "EnvMapGlowsCount"
     */
    arrayCountFor0x68: number;

    /**
     * "FlaresCount"
     */
    arrayCountFor0x64: number;

    /**
     * "GlowsCount"
     */
    arrayCountFor0x6c: number;
    arrayCountFor0xc: number;
    arrayCountFor0x24: number;

    /**
     * "PlanarReflectionGlowsCount"
     */
    arrayCountFor0x70: number;

    /**
     * "RearViewMirrorGlowsCount"
     */
    arrayCountFor0x74: number;
    arrayCountFor0x3c: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenUielementPrototypeScrollingTextString {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.binding0xc = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.gameChangerId0x14 = (this._io.readU4be()) as any
      this.cgsCoreUniqueId0x18 = (this._io.readU4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (28) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3685969725) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    binding0xc: GenericGenObject.StringBase;
    gameChangerId0x14: number;
    cgsCoreUniqueId0x18: number;
  }
}

export namespace GenericGenObject {
  export class T00002eA1 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenLightCone {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenLightBase(this._io, this, this._root)) as any
      this.float32T0x60 = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (100) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3989427985) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenLightBase;
    float32T0x60: number;
  }
}

export namespace GenericGenObject {
  export class D7B221Da {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class RwMathVpuVector4 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.arrInlineElements0x0 = [];
      for (let i = 0; i < 4; i++) {
        this.arrInlineElements0x0.push(this._io.readF4be());
      }
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (4) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3257509935) as any
      return this._muVersionHash;
    }

    arrInlineElements0x0: Array<number>;
  }
}

export namespace GenericGenObject {
  export class GenesysGenLayoutSequenceItem {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenSequenceItem(this._io, this, this._root)) as any
      this.cgsResourceHandle0x20 = (this._io.readBytes(8)) as any
      this.cgsResourceHandle0x28 = (this._io.readBytes(8)) as any
      this.unkEnum0x30 = (this._io.readU4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (52) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2878684940) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenSequenceItem;
    cgsResourceHandle0x20: Uint8Array;
    cgsResourceHandle0x28: Uint8Array;

    /**
     * enum; 00_03_f8_50_1
     */
    unkEnum0x30: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenEnvironmentKeyframeWeather {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.float32T0x10 = (this._io.readF4be()) as any
      this.float32T0x14 = (this._io.readF4be()) as any
      this.float32T0x18 = (this._io.readF4be()) as any
      this.float32T0x1c = (this._io.readF4be()) as any
      this.float32T0x20 = (this._io.readF4be()) as any
      this.float32T0x24 = (this._io.readF4be()) as any
      this.float32T0x28 = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (44) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3650553990) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    float32T0x10: number;
    float32T0x14: number;
    float32T0x18: number;
    float32T0x1c: number;
    float32T0x20: number;
    float32T0x24: number;
    float32T0x28: number;
  }
}

export namespace GenericGenObject {
  export class CgsResourceHandle {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenArcLightConeUpgrade {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenWeaponUpgrade(this._io, this, this._root)) as any
      this.float32T0x1c = (this._io.readF4be()) as any
      this.float32T0x20 = (this._io.readF4be()) as any
      this.float32T0x24 = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (40) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (4092156414) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenWeaponUpgrade;
    float32T0x1c: number;
    float32T0x20: number;
    float32T0x24: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenCameraShakeSequenceItem {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenSequenceItem(this._io, this, this._root)) as any
      this.unkEnum0x20 = (this._io.readU4be()) as any
    }

    private _inst00068fD810x20: number | undefined;
    get inst00068fD810x20(): number | undefined {
      if (typeof this._inst00068fD810x20 !== 'undefined')
        return this._inst00068fD810x20;
      if ((this.unkEnum0x20 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.unkEnum0x20 as any));
        this._inst00068fD810x20 = (this._io.readU4be()) as any
        this._io.seek(_pos);
      }
      return this._inst00068fD810x20;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (36) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1557152310) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenSequenceItem;

    /**
     * enum; 00_06_8f_d8_1
     */
    unkEnum0x20: number;
  }
}

export namespace GenericGenObject {
  export class T00002fD0 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class T00003038 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class Bool8T {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenPhysicalDefinitionRigidBodyCylinderVolume {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.volumeToBodyTransform0x10 = (new GenericGenObject.RwMathVpuMatrix44affine(this._io, this, this._root)) as any
      this.gameChangerId0x50 = (this._io.readU4be()) as any
      this.halfLength0x54 = (this._io.readF4be()) as any
      this.radius0x58 = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (92) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (18021398) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    volumeToBodyTransform0x10: GenericGenObject.RwMathVpuMatrix44affine;
    gameChangerId0x50: number;
    halfLength0x54: number;
    radius0x58: number;
  }
}

export namespace GenericGenObject {
  export class T00093793 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenPostFxstateValueModifier {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.modificationValue0x10 = (this._io.readF4be()) as any
      this.modificationType0x14 = (this._io.readU4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (24) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (4120564202) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    modificationValue0x10: number;

    /**
     * enum; 00_00_30_3d_1
     */
    modificationType0x14: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenWcvfxBehaviourCoronas {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.coronaDefinition0xc = (this._io.readBytes(8)) as any
      this.gameChangerId0x14 = (this._io.readU4be()) as any
      this.locatorGroup0x18 = (this._io.readU4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (28) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3756202357) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    coronaDefinition0xc: Uint8Array;
    gameChangerId0x14: number;
    locatorGroup0x18: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenImpactDamageGameRule {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenGameRule(this._io, this, this._root)) as any
      this.back0x10 = (this._io.readF4be()) as any
      this.float32T0x14 = (this._io.readF4be()) as any
      this.float32T0x18 = (this._io.readF4be()) as any
      this.float32T0x1c = (this._io.readF4be()) as any
      this.float32T0x20 = (this._io.readF4be()) as any
      this.float32T0x24 = (this._io.readF4be()) as any
      this.float32T0x28 = (this._io.readF4be()) as any
      this.left0x2c = (this._io.readF4be()) as any
      this.float32T0x30 = (this._io.readF4be()) as any
      this.float32T0x34 = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (56) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (437108292) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenGameRule;
    back0x10: number;
    float32T0x14: number;
    float32T0x18: number;
    float32T0x1c: number;
    float32T0x20: number;
    float32T0x24: number;
    float32T0x28: number;
    left0x2c: number;
    float32T0x30: number;
    float32T0x34: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenGameMode {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.cgsCoreStringBase0xc = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.hudHsm0x14 = (this._io.readBytes(8)) as any
      this.description0x1c = (this._io.readU4be()) as any
      this.gameChangerId0x20 = (this._io.readU4be()) as any
      this.hsm0x24 = (this._io.readU4be()) as any
      this.cgsCoreUniqueId0x28 = (this._io.readU4be()) as any
      this.mixSnapShot0x2c = (this._io.readU4be()) as any
      this.name0x30 = (this._io.readU4be()) as any
      this.scoreViewModel0x34 = (this._io.readU4be()) as any
      this.weaponList0x38 = (this._io.readU4be()) as any
      this.modeIntroTimeLimit0x3c = (this._io.readF4be()) as any
      this.modeTimeLimit0x40 = (this._io.readF4be()) as any
      this.float32T0x44 = (this._io.readF4be()) as any
      this.unkEnum0x48 = (this._io.readU4be()) as any
      this.interceptingCopFrequency0x4c = (this._io.readS4be()) as any
      this.minimapDistance0x50 = (this._io.readS4be()) as any
      this.modeScoreLimit0x54 = (this._io.readS4be()) as any
      this.oncomingCopFrequency0x58 = (this._io.readS4be()) as any
      this.int32T0x5c = (this._io.readS4be()) as any
      this.trailingCopFrequency0x60 = (this._io.readS4be()) as any
      this.rankingType0x64 = (this._io.readU2be()) as any
      this.arrayCountFor0x48 = (this._io.readU2be()) as any
      this.allowAiracerDamageFromWorld0x68 = (this._io.readU1()) as any
      this.allowFriendlyFire0x69 = (this._io.readU1()) as any
      this.hostCanEndGame0x6a = (this._io.readU1()) as any
      this.bool8T0x6b = (this._io.readU1()) as any
      this.online0x6c = (this._io.readU1()) as any
      this.bool8T0x6d = (this._io.readU1()) as any
      this.retryEnabled0x6e = (this._io.readU1()) as any
      this.bool8T0x6f = (this._io.readU1()) as any
      this.spawnTowardsAi0x70 = (this._io.readU1()) as any
      this.teamGame0x71 = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _inst0004613510x48: Array<number | undefined> | undefined;
    get inst0004613510x48(): Array<number | undefined> | undefined {
      if (typeof this._inst0004613510x48 !== 'undefined')
        return this._inst0004613510x48;
      if ((this.unkEnum0x48 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.unkEnum0x48 as any));
        this._inst0004613510x48 = [];
        for (let i = 0; i < (this.arrayCountFor0x48 as any); i++) {
          this._inst0004613510x48.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._inst0004613510x48;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (116) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1137921905) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    cgsCoreStringBase0xc: GenericGenObject.StringBase;
    hudHsm0x14: Uint8Array;
    description0x1c: number;
    gameChangerId0x20: number;
    hsm0x24: number;
    cgsCoreUniqueId0x28: number;
    mixSnapShot0x2c: number;
    name0x30: number;
    scoreViewModel0x34: number;
    weaponList0x38: number;
    modeIntroTimeLimit0x3c: number;
    modeTimeLimit0x40: number;
    float32T0x44: number;

    /**
     * enum; 00_04_61_35_1
     */
    unkEnum0x48: number;
    interceptingCopFrequency0x4c: number;
    minimapDistance0x50: number;
    modeScoreLimit0x54: number;
    oncomingCopFrequency0x58: number;
    int32T0x5c: number;
    trailingCopFrequency0x60: number;

    /**
     * enum; 00_05_f7_0e_1
     */
    rankingType0x64: number;
    arrayCountFor0x48: number;
    allowAiracerDamageFromWorld0x68: number;
    allowFriendlyFire0x69: number;
    hostCanEndGame0x6a: number;
    bool8T0x6b: number;
    online0x6c: number;
    bool8T0x6d: number;
    retryEnabled0x6e: number;
    bool8T0x6f: number;
    spawnTowardsAi0x70: number;
    teamGame0x71: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenUielementBaseBehaviour {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.cgsCoreStringBase0xc = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.gameChangerId0x14 = (this._io.readU4be()) as any
      this.cgsCoreUniqueId0x18 = (this._io.readU4be()) as any
      this.float32T0x1c = (this._io.readF4be()) as any
      this.duration0x20 = (this._io.readF4be()) as any
      this.type0x24 = (this._io.readU2be()) as any
      this.ease0x26 = (this._io.readU2be()) as any
      this.unkEnum0x28 = (this._io.readU4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (44) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (327168116) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    cgsCoreStringBase0xc: GenericGenObject.StringBase;
    gameChangerId0x14: number;
    cgsCoreUniqueId0x18: number;
    float32T0x1c: number;
    duration0x20: number;

    /**
     * enum; 35_d6_2d_64
     */
    type0x24: number;

    /**
     * enum; 5b_33_21_f5
     */
    ease0x26: number;

    /**
     * enum; 34_26_5a_75
     */
    unkEnum0x28: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenEventArena {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.arenaData0xc = (this._io.readU4be()) as any
      this.gameChangerId0x10 = (this._io.readU4be()) as any
      this.image0x14 = (this._io.readU4be()) as any
      this.map0x18 = (this._io.readU4be()) as any
      this.name0x1c = (this._io.readU4be()) as any
      this.world0x20 = (this._io.readU4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (36) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2545624958) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    arenaData0xc: number;
    gameChangerId0x10: number;
    image0x14: number;
    map0x18: number;
    name0x1c: number;
    world0x20: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenGamePack {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.name0xc = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.carPackImage0x14 = (this._io.readU4be()) as any
      this.displayName0x18 = (this._io.readU4be()) as any
      this.gameChangerId0x1c = (this._io.readU4be()) as any
      this.showPackOnEntitlement0x20 = (this._io.readU4be()) as any
      this.release0x24 = (this._io.readU4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (40) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3562210973) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    name0xc: GenericGenObject.StringBase;
    carPackImage0x14: number;
    displayName0x18: number;
    gameChangerId0x1c: number;
    showPackOnEntitlement0x20: number;

    /**
     * enum; 00_00_2f_c8_1
     */
    release0x24: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenHeatLevelCopType {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.aiplayerType0xc = (this._io.readU4be()) as any
      this.gameChangerId0x10 = (this._io.readU4be()) as any
      this.bool8T0x14 = (this._io.readU1()) as any
      this.canSpawnBehind0x15 = (this._io.readU1()) as any
      this.canSpawnHeadOn0x16 = (this._io.readU1()) as any
      this.canSpawnIntercepting0x17 = (this._io.readU1()) as any
      this.uint8T0x18 = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(3)) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (28) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2048015465) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    aiplayerType0xc: number;
    gameChangerId0x10: number;
    bool8T0x14: number;
    canSpawnBehind0x15: number;
    canSpawnHeadOn0x16: number;
    canSpawnIntercepting0x17: number;
    uint8T0x18: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenUielementPrototypeScrollingTextTextProperties {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.rwMathVpuVector40x10 = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
      this.cgsCoreStringBase0x20 = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.cgsResourceHandle0x28 = (this._io.readBytes(8)) as any
      this.gameChangerId0x30 = (this._io.readU4be()) as any
      this.unoO0x34 = (this._io.readU2be()) as any
      this.bool8T0x36 = (this._io.readU1()) as any
      this.bool8T0x37 = (this._io.readU1()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (56) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (4168741296) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    rwMathVpuVector40x10: GenericGenObject.RwMathVpuVector4;
    cgsCoreStringBase0x20: GenericGenObject.StringBase;
    cgsResourceHandle0x28: Uint8Array;
    gameChangerId0x30: number;

    /**
     * enum; f7_ff_d1_f8
     */
    unoO0x34: number;
    bool8T0x36: number;
    bool8T0x37: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenRoadBlockDefinition {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.ptrArrBackLayers0xc = (this._io.readU4be()) as any
      this.ptrArrFrontLayers0x10 = (this._io.readU4be()) as any
      this.gameChangerId0x14 = (this._io.readU4be()) as any
      this.primaryLayer0x18 = (this._io.readU4be()) as any
      this.layerDistance0x1c = (this._io.readF4be()) as any
      this.arrayCountFor0xc = (this._io.readU2be()) as any
      this.arrayCountFor0x10 = (this._io.readU2be()) as any
    }

    private _instBackLayers0xc: Array<number | undefined> | undefined;
    get instBackLayers0xc(): Array<number | undefined> | undefined {
      if (typeof this._instBackLayers0xc !== 'undefined')
        return this._instBackLayers0xc;
      if ((this.ptrArrBackLayers0xc as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrBackLayers0xc as any));
        this._instBackLayers0xc = [];
        for (let i = 0; i < (this.arrayCountFor0xc as any); i++) {
          this._instBackLayers0xc.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._instBackLayers0xc;
    }

    private _instFrontLayers0x10: Array<number | undefined> | undefined;
    get instFrontLayers0x10(): Array<number | undefined> | undefined {
      if (typeof this._instFrontLayers0x10 !== 'undefined')
        return this._instFrontLayers0x10;
      if ((this.ptrArrFrontLayers0x10 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrFrontLayers0x10 as any));
        this._instFrontLayers0x10 = [];
        for (let i = 0; i < (this.arrayCountFor0x10 as any); i++) {
          this._instFrontLayers0x10.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._instFrontLayers0x10;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (36) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2953390990) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    ptrArrBackLayers0xc: number;
    ptrArrFrontLayers0x10: number;
    gameChangerId0x14: number;
    primaryLayer0x18: number;
    layerDistance0x1c: number;

    /**
     * "BackLayersCount"
     */
    arrayCountFor0xc: number;

    /**
     * "FrontLayersCount"
     */
    arrayCountFor0x10: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenPerk {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.ptrArrCgsResourceHandle0x10 = (this._io.readU4be()) as any
      this.arrayCountFor0x10 = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(3)) as any
    }

    private _instCgsResourceHandle0x10: Array<GenericGenObject.CgsResourceHandle | undefined> | undefined;
    get instCgsResourceHandle0x10(): Array<GenericGenObject.CgsResourceHandle | undefined> | undefined {
      if (typeof this._instCgsResourceHandle0x10 !== 'undefined')
        return this._instCgsResourceHandle0x10;
      if ((this.ptrArrCgsResourceHandle0x10 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrCgsResourceHandle0x10 as any));
        this._instCgsResourceHandle0x10 = [];
        for (let i = 0; i < (this.arrayCountFor0x10 as any); i++) {
          this._instCgsResourceHandle0x10.push(new GenericGenObject.CgsResourceHandle(this._io, this, this._root));
        }
        this._io.seek(_pos);
      }
      return this._instCgsResourceHandle0x10;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (24) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (838894301) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    ptrArrCgsResourceHandle0x10: number;
    arrayCountFor0x10: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class T0003F683 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class PtrPtr {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: unknown | undefined,
      readonly _root: GenericGenObject | undefined,
      dtype: string,
    ) {
      this.dtype = dtype;

      this._read();
    }

    _read() {
      this.offset = (this._io.readS4be()) as any
    }

    private _ptr: GenericGenObject.Ptr | undefined;
    get ptr(): GenericGenObject.Ptr | undefined {
      if (typeof this._ptr !== 'undefined')
        return this._ptr;
      if ((this.offset as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.offset as any));
        this._ptr = (new GenericGenObject.Ptr(this._io, this, this._root, (this.dtype as any))) as any
        this._io.seek(_pos);
      }
      return this._ptr;
    }

    offset: number;
    dtype: string;
  }
}

export namespace GenericGenObject {
  export class GenesysGenExtraAmmoWeaponUpgrade {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenWeaponUpgrade(this._io, this, this._root)) as any
      this.uint8T0x1c = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(3)) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (32) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1658948550) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenWeaponUpgrade;
    uint8T0x1c: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenWeaponRechargeData {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.float32T0x10 = (this._io.readF4be()) as any
      this.float32T0x14 = (this._io.readF4be()) as any
      this.float32T0x18 = (this._io.readF4be()) as any
      this.float32T0x1c = (this._io.readF4be()) as any
      this.type0x20 = (this._io.readU4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (36) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3688569486) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    float32T0x10: number;
    float32T0x14: number;
    float32T0x18: number;
    float32T0x1c: number;

    /**
     * enum; 00_07_57_09_1
     */
    type0x20: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenPhysicalDefinitionRigidBody {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.bodyToObjectTransform0x10 = (new GenericGenObject.RwMathVpuMatrix44affine(this._io, this, this._root)) as any
      this.comOffset0x50 = (new GenericGenObject.RwMathVpuVector3(this._io, this, this._root)) as any
      this.inertiaScale0x60 = (new GenericGenObject.RwMathVpuVector3(this._io, this, this._root)) as any
      this.localAabbcenter0x70 = (new GenericGenObject.RwMathVpuVector3(this._io, this, this._root)) as any
      this.localAabbhalfDiagonal0x80 = (new GenericGenObject.RwMathVpuVector3(this._io, this, this._root)) as any
      this.ptrArrSymmetricalInAxis0x90 = (this._io.readU4be()) as any
      this.gameChangerId0x94 = (this._io.readU4be()) as any
      this.angularDrag0x98 = (this._io.readF4be()) as any
      this.bounciness0x9c = (this._io.readF4be()) as any
      this.friction0xa0 = (this._io.readF4be()) as any
      this.linearDrag0xa4 = (this._io.readF4be()) as any
      this.mass0xa8 = (this._io.readF4be()) as any
      this.ptrArrBoxVolumes0xac = (this._io.readU4be()) as any
      this.ptrArrCapsuleVolumes0xb0 = (this._io.readU4be()) as any
      this.ptrArrConvexHullVolumes0xb4 = (this._io.readU4be()) as any
      this.ptrArrCylinderVolumes0xb8 = (this._io.readU4be()) as any
      this.ptrArrSphereVolumes0xbc = (this._io.readU4be()) as any
      this.arrayCountFor0xac = (this._io.readU2be()) as any
      this.arrayCountFor0xb0 = (this._io.readU2be()) as any
      this.arrayCountFor0xb4 = (this._io.readU2be()) as any
      this.arrayCountFor0xb8 = (this._io.readU2be()) as any
      this.arrayCountFor0xbc = (this._io.readU2be()) as any
      this.arrayCountFor0x90 = (this._io.readU2be()) as any
      this.isWheel0xcc = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(3)) as any
    }

    private _instCapsuleVolumes0xb0: Array<GenericGenObject.GenesysGenPhysicalDefinitionRigidBodyCapsuleVolume | undefined> | undefined;
    get instCapsuleVolumes0xb0(): Array<GenericGenObject.GenesysGenPhysicalDefinitionRigidBodyCapsuleVolume | undefined> | undefined {
      if (typeof this._instCapsuleVolumes0xb0 !== 'undefined')
        return this._instCapsuleVolumes0xb0;
      if ((this.ptrArrCapsuleVolumes0xb0 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrCapsuleVolumes0xb0 as any));
        this._instCapsuleVolumes0xb0 = [];
        for (let i = 0; i < (this.arrayCountFor0xb0 as any); i++) {
          this._instCapsuleVolumes0xb0.push(new GenericGenObject.GenesysGenPhysicalDefinitionRigidBodyCapsuleVolume(this._io, this, this._root));
        }
        this._io.seek(_pos);
      }
      return this._instCapsuleVolumes0xb0;
    }

    private _instBoxVolumes0xac: Array<GenericGenObject.GenesysGenPhysicalDefinitionRigidBodyBoxVolume | undefined> | undefined;
    get instBoxVolumes0xac(): Array<GenericGenObject.GenesysGenPhysicalDefinitionRigidBodyBoxVolume | undefined> | undefined {
      if (typeof this._instBoxVolumes0xac !== 'undefined')
        return this._instBoxVolumes0xac;
      if ((this.ptrArrBoxVolumes0xac as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrBoxVolumes0xac as any));
        this._instBoxVolumes0xac = [];
        for (let i = 0; i < (this.arrayCountFor0xac as any); i++) {
          this._instBoxVolumes0xac.push(new GenericGenObject.GenesysGenPhysicalDefinitionRigidBodyBoxVolume(this._io, this, this._root));
        }
        this._io.seek(_pos);
      }
      return this._instBoxVolumes0xac;
    }

    private _instConvexHullVolumes0xb4: Array<GenericGenObject.GenesysGenPhysicalDefinitionRigidBodyConvexHullVolume | undefined> | undefined;
    get instConvexHullVolumes0xb4(): Array<GenericGenObject.GenesysGenPhysicalDefinitionRigidBodyConvexHullVolume | undefined> | undefined {
      if (typeof this._instConvexHullVolumes0xb4 !== 'undefined')
        return this._instConvexHullVolumes0xb4;
      if ((this.ptrArrConvexHullVolumes0xb4 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrConvexHullVolumes0xb4 as any));
        this._instConvexHullVolumes0xb4 = [];
        for (let i = 0; i < (this.arrayCountFor0xb4 as any); i++) {
          this._instConvexHullVolumes0xb4.push(new GenericGenObject.GenesysGenPhysicalDefinitionRigidBodyConvexHullVolume(this._io, this, this._root));
        }
        this._io.seek(_pos);
      }
      return this._instConvexHullVolumes0xb4;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (208) as any
      return this._size;
    }

    private _instCylinderVolumes0xb8: Array<GenericGenObject.GenesysGenPhysicalDefinitionRigidBodyCylinderVolume | undefined> | undefined;
    get instCylinderVolumes0xb8(): Array<GenericGenObject.GenesysGenPhysicalDefinitionRigidBodyCylinderVolume | undefined> | undefined {
      if (typeof this._instCylinderVolumes0xb8 !== 'undefined')
        return this._instCylinderVolumes0xb8;
      if ((this.ptrArrCylinderVolumes0xb8 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrCylinderVolumes0xb8 as any));
        this._instCylinderVolumes0xb8 = [];
        for (let i = 0; i < (this.arrayCountFor0xb8 as any); i++) {
          this._instCylinderVolumes0xb8.push(new GenericGenObject.GenesysGenPhysicalDefinitionRigidBodyCylinderVolume(this._io, this, this._root));
        }
        this._io.seek(_pos);
      }
      return this._instCylinderVolumes0xb8;
    }

    private _instSphereVolumes0xbc: Array<GenericGenObject.GenesysGenPhysicalDefinitionRigidBodySphereVolume | undefined> | undefined;
    get instSphereVolumes0xbc(): Array<GenericGenObject.GenesysGenPhysicalDefinitionRigidBodySphereVolume | undefined> | undefined {
      if (typeof this._instSphereVolumes0xbc !== 'undefined')
        return this._instSphereVolumes0xbc;
      if ((this.ptrArrSphereVolumes0xbc as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrSphereVolumes0xbc as any));
        this._instSphereVolumes0xbc = [];
        for (let i = 0; i < (this.arrayCountFor0xbc as any); i++) {
          this._instSphereVolumes0xbc.push(new GenericGenObject.GenesysGenPhysicalDefinitionRigidBodySphereVolume(this._io, this, this._root));
        }
        this._io.seek(_pos);
      }
      return this._instSphereVolumes0xbc;
    }

    private _instSymmetricalInAxis0x90: Array<number | undefined> | undefined;
    get instSymmetricalInAxis0x90(): Array<number | undefined> | undefined {
      if (typeof this._instSymmetricalInAxis0x90 !== 'undefined')
        return this._instSymmetricalInAxis0x90;
      if ((this.ptrArrSymmetricalInAxis0x90 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrSymmetricalInAxis0x90 as any));
        this._instSymmetricalInAxis0x90 = [];
        for (let i = 0; i < (this.arrayCountFor0x90 as any); i++) {
          this._instSymmetricalInAxis0x90.push(this._io.readU1());
        }
        this._io.seek(_pos);
      }
      return this._instSymmetricalInAxis0x90;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2362053299) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    bodyToObjectTransform0x10: GenericGenObject.RwMathVpuMatrix44affine;
    comOffset0x50: GenericGenObject.RwMathVpuVector3;
    inertiaScale0x60: GenericGenObject.RwMathVpuVector3;
    localAabbcenter0x70: GenericGenObject.RwMathVpuVector3;
    localAabbhalfDiagonal0x80: GenericGenObject.RwMathVpuVector3;
    ptrArrSymmetricalInAxis0x90: number;
    gameChangerId0x94: number;
    angularDrag0x98: number;
    bounciness0x9c: number;
    friction0xa0: number;
    linearDrag0xa4: number;
    mass0xa8: number;
    ptrArrBoxVolumes0xac: number;
    ptrArrCapsuleVolumes0xb0: number;
    ptrArrConvexHullVolumes0xb4: number;
    ptrArrCylinderVolumes0xb8: number;
    ptrArrSphereVolumes0xbc: number;

    /**
     * "BoxVolumesCount"
     */
    arrayCountFor0xac: number;

    /**
     * "CapsuleVolumesCount"
     */
    arrayCountFor0xb0: number;

    /**
     * "ConvexHullVolumesCount"
     */
    arrayCountFor0xb4: number;

    /**
     * "CylinderVolumesCount"
     */
    arrayCountFor0xb8: number;

    /**
     * "SphereVolumesCount"
     */
    arrayCountFor0xbc: number;

    /**
     * "SymmetricalInAxisCount"
     */
    arrayCountFor0x90: number;
    isWheel0xcc: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class T34265a75 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenJammerWeapon {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenWeapon(this._io, this, this._root)) as any
      this.effectDuration0xb0 = (this._io.readF4be()) as any
      this.float32T0xb4 = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (184) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3309031391) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenWeapon;
    effectDuration0xb0: number;
    float32T0xb4: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenUielementBaseTimeline {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.cgsCoreStringBase0xc = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.cgsCoreStringBase0x14 = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.gameChangerId0x1c = (this._io.readU4be()) as any
      this.ptrArrGenesysGenUielementBaseTimelineBehaviour0x20 = (this._io.readU4be()) as any
      this.ptrArrGenesysGenUielementBaseTimelineBehaviour0x24 = (this._io.readU4be()) as any
      this.ptrArrGenesysGenUielementBaseTimelineBehaviour0x28 = (this._io.readU4be()) as any
      this.int32T0x2c = (this._io.readS4be()) as any
      this.unkEnum0x30 = (this._io.readU2be()) as any
      this.arrayCountFor0x20 = (this._io.readU2be()) as any
      this.arrayCountFor0x24 = (this._io.readU2be()) as any
      this.arrayCountFor0x28 = (this._io.readU2be()) as any
    }

    private _instGenesysGenUielementBaseTimelineBehaviour0x28: Array<GenericGenObject.GenesysGenUielementBaseTimelineBehaviour | undefined> | undefined;
    get instGenesysGenUielementBaseTimelineBehaviour0x28(): Array<GenericGenObject.GenesysGenUielementBaseTimelineBehaviour | undefined> | undefined {
      if (typeof this._instGenesysGenUielementBaseTimelineBehaviour0x28 !== 'undefined')
        return this._instGenesysGenUielementBaseTimelineBehaviour0x28;
      if ((this.ptrArrGenesysGenUielementBaseTimelineBehaviour0x28 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrGenesysGenUielementBaseTimelineBehaviour0x28 as any));
        this._instGenesysGenUielementBaseTimelineBehaviour0x28 = [];
        for (let i = 0; i < (this.arrayCountFor0x28 as any); i++) {
          this._instGenesysGenUielementBaseTimelineBehaviour0x28.push(new GenericGenObject.GenesysGenUielementBaseTimelineBehaviour(this._io, this, this._root));
        }
        this._io.seek(_pos);
      }
      return this._instGenesysGenUielementBaseTimelineBehaviour0x28;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (56) as any
      return this._size;
    }

    private _instGenesysGenUielementBaseTimelineBehaviour0x20: Array<GenericGenObject.GenesysGenUielementBaseTimelineBehaviour | undefined> | undefined;
    get instGenesysGenUielementBaseTimelineBehaviour0x20(): Array<GenericGenObject.GenesysGenUielementBaseTimelineBehaviour | undefined> | undefined {
      if (typeof this._instGenesysGenUielementBaseTimelineBehaviour0x20 !== 'undefined')
        return this._instGenesysGenUielementBaseTimelineBehaviour0x20;
      if ((this.ptrArrGenesysGenUielementBaseTimelineBehaviour0x20 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrGenesysGenUielementBaseTimelineBehaviour0x20 as any));
        this._instGenesysGenUielementBaseTimelineBehaviour0x20 = [];
        for (let i = 0; i < (this.arrayCountFor0x20 as any); i++) {
          this._instGenesysGenUielementBaseTimelineBehaviour0x20.push(new GenericGenObject.GenesysGenUielementBaseTimelineBehaviour(this._io, this, this._root));
        }
        this._io.seek(_pos);
      }
      return this._instGenesysGenUielementBaseTimelineBehaviour0x20;
    }

    private _instGenesysGenUielementBaseTimelineBehaviour0x24: Array<GenericGenObject.GenesysGenUielementBaseTimelineBehaviour | undefined> | undefined;
    get instGenesysGenUielementBaseTimelineBehaviour0x24(): Array<GenericGenObject.GenesysGenUielementBaseTimelineBehaviour | undefined> | undefined {
      if (typeof this._instGenesysGenUielementBaseTimelineBehaviour0x24 !== 'undefined')
        return this._instGenesysGenUielementBaseTimelineBehaviour0x24;
      if ((this.ptrArrGenesysGenUielementBaseTimelineBehaviour0x24 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrGenesysGenUielementBaseTimelineBehaviour0x24 as any));
        this._instGenesysGenUielementBaseTimelineBehaviour0x24 = [];
        for (let i = 0; i < (this.arrayCountFor0x24 as any); i++) {
          this._instGenesysGenUielementBaseTimelineBehaviour0x24.push(new GenericGenObject.GenesysGenUielementBaseTimelineBehaviour(this._io, this, this._root));
        }
        this._io.seek(_pos);
      }
      return this._instGenesysGenUielementBaseTimelineBehaviour0x24;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2925930439) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    cgsCoreStringBase0xc: GenericGenObject.StringBase;
    cgsCoreStringBase0x14: GenericGenObject.StringBase;
    gameChangerId0x1c: number;
    ptrArrGenesysGenUielementBaseTimelineBehaviour0x20: number;
    ptrArrGenesysGenUielementBaseTimelineBehaviour0x24: number;
    ptrArrGenesysGenUielementBaseTimelineBehaviour0x28: number;
    int32T0x2c: number;

    /**
     * enum; c9_7e_aa_da
     */
    unkEnum0x30: number;
    arrayCountFor0x20: number;
    arrayCountFor0x24: number;
    arrayCountFor0x28: number;
  }
}

export namespace GenericGenObject {
  export class Int16T {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class T0589A977 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenGameUnlockEvent {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.cgsCoreUniqueId0xc = (this._io.readU4be()) as any
      this.gameChangerId0x10 = (this._io.readU4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (20) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1375788276) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    cgsCoreUniqueId0xc: number;
    gameChangerId0x10: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenEventList {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.ptrArrOrderedList0x10 = (this._io.readU4be()) as any
      this.arrayCountFor0x10 = (this._io.readU2be()) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _instOrderedList0x10: Array<number | undefined> | undefined;
    get instOrderedList0x10(): Array<number | undefined> | undefined {
      if (typeof this._instOrderedList0x10 !== 'undefined')
        return this._instOrderedList0x10;
      if ((this.ptrArrOrderedList0x10 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrOrderedList0x10 as any));
        this._instOrderedList0x10 = [];
        for (let i = 0; i < (this.arrayCountFor0x10 as any); i++) {
          this._instOrderedList0x10.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._instOrderedList0x10;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (24) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (981367156) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    ptrArrOrderedList0x10: number;

    /**
     * "OrderedListCount"
     */
    arrayCountFor0x10: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenTeflonSlickWeapon {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenWeapon(this._io, this, this._root)) as any
      this.cgsCoreUniqueId0xb0 = (this._io.readU4be()) as any
      this.cgsCoreUniqueId0xb4 = (this._io.readU4be()) as any
      this.float32T0xb8 = (this._io.readF4be()) as any
      this.float32T0xbc = (this._io.readF4be()) as any
      this.float32T0xc0 = (this._io.readF4be()) as any
      this.float32T0xc4 = (this._io.readF4be()) as any
      this.float32T0xc8 = (this._io.readF4be()) as any
      this.radius0xcc = (this._io.readF4be()) as any
      this.float32T0xd0 = (this._io.readF4be()) as any
      this.float32T0xd4 = (this._io.readF4be()) as any
      this.int32T0xd8 = (this._io.readS4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (220) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1859689840) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenWeapon;
    cgsCoreUniqueId0xb0: number;
    cgsCoreUniqueId0xb4: number;
    float32T0xb8: number;
    float32T0xbc: number;
    float32T0xc0: number;
    float32T0xc4: number;
    float32T0xc8: number;
    radius0xcc: number;
    float32T0xd0: number;
    float32T0xd4: number;
    int32T0xd8: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenUimaterial {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.material0x10 = (this._io.readU4be()) as any
      this.ptrArrCgsResourceHandle0x14 = (this._io.readU4be()) as any
      this.int32T0x18 = (this._io.readS4be()) as any
      this.unkEnum0x1c = (this._io.readU2be()) as any
      this.arrayCountFor0x14 = (this._io.readU2be()) as any
    }

    private _instCgsResourceHandle0x14: Array<GenericGenObject.CgsResourceHandle | undefined> | undefined;
    get instCgsResourceHandle0x14(): Array<GenericGenObject.CgsResourceHandle | undefined> | undefined {
      if (typeof this._instCgsResourceHandle0x14 !== 'undefined')
        return this._instCgsResourceHandle0x14;
      if ((this.ptrArrCgsResourceHandle0x14 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrCgsResourceHandle0x14 as any));
        this._instCgsResourceHandle0x14 = [];
        for (let i = 0; i < (this.arrayCountFor0x14 as any); i++) {
          this._instCgsResourceHandle0x14.push(new GenericGenObject.CgsResourceHandle(this._io, this, this._root));
        }
        this._io.seek(_pos);
      }
      return this._instCgsResourceHandle0x14;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (32) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2027355840) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    material0x10: number;
    ptrArrCgsResourceHandle0x14: number;
    int32T0x18: number;

    /**
     * enum; 00_06_cc_2f_1
     */
    unkEnum0x1c: number;
    arrayCountFor0x14: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenSilentLaunchWeaponUpgrade {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenWeaponUpgrade(this._io, this, this._root)) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (28) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1284749351) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenWeaponUpgrade;
  }
}

export namespace GenericGenObject {
  export class GenesysGenUilayoutInstanceParamsTransformComponents {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.binding0xc = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.gameChangerId0x14 = (this._io.readU4be()) as any
      this.x0x18 = (this._io.readF4be()) as any
      this.y0x1c = (this._io.readF4be()) as any
      this.z0x20 = (this._io.readF4be()) as any
      this.type0x24 = (this._io.readU4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (40) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1830374425) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    binding0xc: GenericGenObject.StringBase;
    gameChangerId0x14: number;
    x0x18: number;
    y0x1c: number;
    z0x20: number;

    /**
     * enum; 00_00_31_ca_1
     */
    type0x24: number;
  }
}

export namespace GenericGenObject {
  export class PtrArray {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: unknown | undefined,
      readonly _root: GenericGenObject | undefined,
      dtype: string,
      amt: number,
    ) {
      this.dtype = dtype;
      this.amt = amt;

      this._read();
    }

    _read() {
      this.offset = (this._io.readS4be()) as any
    }

    private _entries: Array<GenericGenObject.Atype>;
    get entries(): Array<GenericGenObject.Atype> {
      if (typeof this._entries !== 'undefined')
        return this._entries;
      let _pos = this._io.pos;
      this._io.seek((this.offset as any));
      this._entries = [];
      for (let i = 0; i < (this.amt as any); i++) {
        this._entries.push(new GenericGenObject.Atype(this._io, this, this._root, (this.dtype as any)));
      }
      this._io.seek(_pos);
      return this._entries;
    }

    offset: number;
    dtype: string;
    amt: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenSpikeStripBodyBlowUpgrade {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenWeaponUpgrade(this._io, this, this._root)) as any
      this.float32T0x1c = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (32) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1441812963) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenWeaponUpgrade;
    float32T0x1c: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenLightPoint {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenLightBase(this._io, this, this._root)) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (88) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3975851796) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenLightBase;
  }
}

export namespace GenericGenObject {
  export class GenesysGenBehaviour {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.label0xc = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.gameChangerId0x14 = (this._io.readU4be()) as any
      this.activateOnHit0x18 = (this._io.readU1()) as any
      this.deactivateOnHit0x19 = (this._io.readU1()) as any
      this.initiallyOn0x1a = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(1)) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (28) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (160896465) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    label0xc: GenericGenObject.StringBase;
    gameChangerId0x14: number;
    activateOnHit0x18: number;
    deactivateOnHit0x19: number;
    initiallyOn0x1a: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenPhysicalExplosion {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.unkEnum0xc = (this._io.readU1()) as any
      this.unkEnum0x30 = (this._io.readU1()) as any
      this.unkEnum0x48 = (this._io.readU1()) as any
      this.unkEnum0x60 = (this._io.readU1()) as any
      this.gameChangerId0x78 = (this._io.readU4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (124) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1819824028) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;

    /**
     * enum; 00_05_d7_a4_1
     */
    unkEnum0xc: number;

    /**
     * enum; 00_05_d7_a7_1
     */
    unkEnum0x30: number;

    /**
     * enum; 00_05_d7_a6_1
     */
    unkEnum0x48: number;

    /**
     * enum; 00_05_d7_a5_1
     */
    unkEnum0x60: number;
    gameChangerId0x78: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenThankYouScreenItem {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.heading0x10 = (this._io.readU4be()) as any
      this.message0x14 = (this._io.readU4be()) as any
      this.bountyReward0x18 = (this._io.readS4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (28) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2578912561) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    heading0x10: number;
    message0x14: number;
    bountyReward0x18: number;
  }
}

export namespace GenericGenObject {
  export class T0c966a95 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenLightBaseFlashPattern {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.duration0x10 = (this._io.readF4be()) as any
      this.frequency0x14 = (this._io.readF4be()) as any
      this.float32T0x18 = (this._io.readF4be()) as any
      this.offset0x1c = (this._io.readF4be()) as any
      this.type0x20 = (this._io.readU4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (36) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (306714612) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    duration0x10: number;
    frequency0x14: number;
    float32T0x18: number;
    offset0x1c: number;

    /**
     * enum; 00_00_2f_f0_1
     */
    type0x20: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenUilayout {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.ptrArrPtrElements0x10 = (this._io.readU4be()) as any
      this.arrayCountFor0x10 = (this._io.readU2be()) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _instElements0x10: Array<GenericGenObject.Ptr | undefined> | undefined;

    /**
     * 'instance of Genesys.Object'
     */
    get instElements0x10(): Array<GenericGenObject.Ptr | undefined> | undefined {
      if (typeof this._instElements0x10 !== 'undefined')
        return this._instElements0x10;
      if ((this.ptrArrPtrElements0x10 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrPtrElements0x10 as any));
        this._instElements0x10 = [];
        for (let i = 0; i < (this.arrayCountFor0x10 as any); i++) {
          this._instElements0x10.push(new GenericGenObject.Ptr(this._io, this, this._root, "generic_gen_object"));
        }
        this._io.seek(_pos);
      }
      return this._instElements0x10;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (24) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2792624488) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    ptrArrPtrElements0x10: number;
    arrayCountFor0x10: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenGameplayTriggerOutput {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.predicate0xc = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.cgsResourceHandle0x14 = (this._io.readBytes(8)) as any
      this.gameChangerId0x1c = (this._io.readU4be()) as any
      this.ptrArrPtrAiplayerInstance0x20 = (this._io.readU4be()) as any
      this.ptrArrSequence0x24 = (this._io.readU4be()) as any
      this.ptrArrPtrRoadblockInstance0x28 = (this._io.readU4be()) as any
      this.arrayCountFor0x24 = (this._io.readU2be()) as any
      this.arrayCountFor0x20 = (this._io.readU1()) as any
      this.arrayCountFor0x28 = (this._io.readU1()) as any
    }

    private _instSequence0x24: Array<number | undefined> | undefined;
    get instSequence0x24(): Array<number | undefined> | undefined {
      if (typeof this._instSequence0x24 !== 'undefined')
        return this._instSequence0x24;
      if ((this.ptrArrSequence0x24 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrSequence0x24 as any));
        this._instSequence0x24 = [];
        for (let i = 0; i < (this.arrayCountFor0x24 as any); i++) {
          this._instSequence0x24.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._instSequence0x24;
    }

    private _instAiplayerInstance0x20: Array<GenericGenObject.Ptr | undefined> | undefined;
    get instAiplayerInstance0x20(): Array<GenericGenObject.Ptr | undefined> | undefined {
      if (typeof this._instAiplayerInstance0x20 !== 'undefined')
        return this._instAiplayerInstance0x20;
      if ((this.ptrArrPtrAiplayerInstance0x20 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrPtrAiplayerInstance0x20 as any));
        this._instAiplayerInstance0x20 = [];
        for (let i = 0; i < (this.arrayCountFor0x20 as any); i++) {
          this._instAiplayerInstance0x20.push(new GenericGenObject.Ptr(this._io, this, this._root, "u4"));
        }
        this._io.seek(_pos);
      }
      return this._instAiplayerInstance0x20;
    }

    private _instRoadblockInstance0x28: Array<GenericGenObject.Ptr | undefined> | undefined;
    get instRoadblockInstance0x28(): Array<GenericGenObject.Ptr | undefined> | undefined {
      if (typeof this._instRoadblockInstance0x28 !== 'undefined')
        return this._instRoadblockInstance0x28;
      if ((this.ptrArrPtrRoadblockInstance0x28 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrPtrRoadblockInstance0x28 as any));
        this._instRoadblockInstance0x28 = [];
        for (let i = 0; i < (this.arrayCountFor0x28 as any); i++) {
          this._instRoadblockInstance0x28.push(new GenericGenObject.Ptr(this._io, this, this._root, "u4"));
        }
        this._io.seek(_pos);
      }
      return this._instRoadblockInstance0x28;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (48) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1454972863) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    predicate0xc: GenericGenObject.StringBase;
    cgsResourceHandle0x14: Uint8Array;
    gameChangerId0x1c: number;

    /**
     * enum; 00_06_fa_75_1
     */
    ptrArrPtrAiplayerInstance0x20: number;

    /**
     * enum; 00_06_cc_76_1
     */
    ptrArrSequence0x24: number;

    /**
     * enum; 00_09_37_62_1
     */
    ptrArrPtrRoadblockInstance0x28: number;

    /**
     * "SequenceCount"
     */
    arrayCountFor0x24: number;
    arrayCountFor0x20: number;

    /**
     * "RoadblockInstanceCount"
     */
    arrayCountFor0x28: number;
  }
}

export namespace GenericGenObject {
  export class T000937A3 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenPhysicalDefinitionRigidBodyCapsuleVolume {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.volumeToBodyTransform0x10 = (new GenericGenObject.RwMathVpuMatrix44affine(this._io, this, this._root)) as any
      this.gameChangerId0x50 = (this._io.readU4be()) as any
      this.halfLength0x54 = (this._io.readF4be()) as any
      this.radius0x58 = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (92) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (18021398) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    volumeToBodyTransform0x10: GenericGenObject.RwMathVpuMatrix44affine;
    gameChangerId0x50: number;
    halfLength0x54: number;
    radius0x58: number;
  }
}

export namespace GenericGenObject {
  export class T00075709 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenFlashBangWeapon {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenWeapon(this._io, this, this._root)) as any
      this.cgsResourceHandle0xb0 = (this._io.readBytes(8)) as any
      this.float32T0xb8 = (this._io.readF4be()) as any
      this.float32T0xbc = (this._io.readF4be()) as any
      this.float32T0xc0 = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (196) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2222312579) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenWeapon;
    cgsResourceHandle0xb0: Uint8Array;
    float32T0xb8: number;
    float32T0xbc: number;
    float32T0xc0: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenNucleusGrantMappingsListMapping {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.nucleusTag0x10 = (this._io.readU4be()) as any
      this.ptrArrEntitlement0x14 = (this._io.readU4be()) as any
      this.arrayCountFor0x14 = (this._io.readU2be()) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _instEntitlement0x14: Array<GenericGenObject.CgsResourceHandle | undefined> | undefined;
    get instEntitlement0x14(): Array<GenericGenObject.CgsResourceHandle | undefined> | undefined {
      if (typeof this._instEntitlement0x14 !== 'undefined')
        return this._instEntitlement0x14;
      if ((this.ptrArrEntitlement0x14 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrEntitlement0x14 as any));
        this._instEntitlement0x14 = [];
        for (let i = 0; i < (this.arrayCountFor0x14 as any); i++) {
          this._instEntitlement0x14.push(new GenericGenObject.CgsResourceHandle(this._io, this, this._root));
        }
        this._io.seek(_pos);
      }
      return this._instEntitlement0x14;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (28) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (4263309034) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    nucleusTag0x10: number;
    ptrArrEntitlement0x14: number;
    arrayCountFor0x14: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenHypoxParticlesWeaponUpgrade {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenWeaponUpgrade(this._io, this, this._root)) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (28) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3895972908) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenWeaponUpgrade;
  }
}

export namespace GenericGenObject {
  export class T000031Ba {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class PtrPtrTable {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: unknown | undefined,
      readonly _root: GenericGenObject | undefined,
      dtype: string,
      amt: number,
    ) {
      this.dtype = dtype;
      this.amt = amt;

      this._read();
    }

    _read() {
      this.offset = (this._io.readS4be()) as any
      if ((this.amt as any) == 0) {
        this.count = (this._io.readU4be()) as any
      }
    }

    private _len: number;
    get len(): number {
      if (typeof this._len !== 'undefined')
        return this._len;
      this._len = (((this.amt as any) == -1 ? 0 : ((this.amt as any) == 0 ? (this.count as any) : (this.amt as any)))) as any
      return this._len;
    }

    private _ptrTable: GenericGenObject.PtrTable | undefined;
    get ptrTable(): GenericGenObject.PtrTable | undefined {
      if (typeof this._ptrTable !== 'undefined')
        return this._ptrTable;
      if ((this.offset as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.offset as any));
        this._ptrTable = (new GenericGenObject.PtrTable(this._io, this, this._root, (this.dtype as any), (this.len as any))) as any
        this._io.seek(_pos);
      }
      return this._ptrTable;
    }

    offset: number;
    count: number | undefined;
    dtype: string;
    amt: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenUielementMoviePlayerDimensions {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.int32T0x10 = (this._io.readS4be()) as any
      this.int32T0x14 = (this._io.readS4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (24) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1386995851) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    int32T0x10: number;
    int32T0x14: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenImpactProtectionGameRule {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenGameRule(this._io, this, this._root)) as any
      this.back0x10 = (this._io.readF4be()) as any
      this.float32T0x14 = (this._io.readF4be()) as any
      this.float32T0x18 = (this._io.readF4be()) as any
      this.float32T0x1c = (this._io.readF4be()) as any
      this.float32T0x20 = (this._io.readF4be()) as any
      this.float32T0x24 = (this._io.readF4be()) as any
      this.float32T0x28 = (this._io.readF4be()) as any
      this.left0x2c = (this._io.readF4be()) as any
      this.float32T0x30 = (this._io.readF4be()) as any
      this.float32T0x34 = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (56) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3993684758) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenGameRule;
    back0x10: number;
    float32T0x14: number;
    float32T0x18: number;
    float32T0x1c: number;
    float32T0x20: number;
    float32T0x24: number;
    float32T0x28: number;
    left0x2c: number;
    float32T0x30: number;
    float32T0x34: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenLightBase {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.colour0x10 = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
      this.unkEnum0x20 = (this._io.readU1()) as any
      this.gameChangerId0x44 = (this._io.readU4be()) as any
      this.float32T0x48 = (this._io.readF4be()) as any
      this.intensity0x4c = (this._io.readF4be()) as any
      this.bool8T0x50 = (this._io.readU1()) as any
      this.bool8T0x51 = (this._io.readU1()) as any
      this.bool8T0x52 = (this._io.readU1()) as any
      this.bool8T0x53 = (this._io.readU1()) as any
      this.bool8T0x54 = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(3)) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (88) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (4046186056) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    colour0x10: GenericGenObject.RwMathVpuVector4;

    /**
     * enum; 00_00_32_f1_1
     */
    unkEnum0x20: number;
    gameChangerId0x44: number;
    float32T0x48: number;
    intensity0x4c: number;
    bool8T0x50: number;
    bool8T0x51: number;
    bool8T0x52: number;
    bool8T0x53: number;
    bool8T0x54: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenEnvironmentKeyframeClouds {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.rwMathVpuVector40x10 = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
      this.rwMathVpuVector40x20 = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
      this.cgsCoreUniqueId0x30 = (this._io.readU4be()) as any
      this.gameChangerId0x34 = (this._io.readU4be()) as any
      this.density0x38 = (this._io.readF4be()) as any
      this.float32T0x3c = (this._io.readF4be()) as any
      this.float32T0x40 = (this._io.readF4be()) as any
      this.scale0x44 = (this._io.readF4be()) as any
      this.float32T0x48 = (this._io.readF4be()) as any
      this.float32T0x4c = (this._io.readF4be()) as any
      this.float32T0x50 = (this._io.readF4be()) as any
      this.speed0x54 = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (88) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (275461846) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    rwMathVpuVector40x10: GenericGenObject.RwMathVpuVector4;
    rwMathVpuVector40x20: GenericGenObject.RwMathVpuVector4;
    cgsCoreUniqueId0x30: number;
    gameChangerId0x34: number;
    density0x38: number;
    float32T0x3c: number;
    float32T0x40: number;
    scale0x44: number;
    float32T0x48: number;
    float32T0x4c: number;
    float32T0x50: number;
    speed0x54: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenScoreViewModelScoreData {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.bindingPath0xc = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.gameChangerId0x14 = (this._io.readU4be()) as any
      this.rank0x18 = (this._io.readS4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (28) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (606909642) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    bindingPath0xc: GenericGenObject.StringBase;
    gameChangerId0x14: number;
    rank0x18: number;
  }
}

export namespace GenericGenObject {
  export class T0005F70e {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenSequenceItemModulatingDoubleValue {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.binding0xc = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.cgsResourceHandle0x14 = (this._io.readBytes(8)) as any
      this.gameChangerId0x1c = (this._io.readU4be()) as any
      this.bias0x20 = (this._io.readF4be()) as any
      this.bindingExponent0x24 = (this._io.readF4be()) as any
      this.bindingRangeMax0x28 = (this._io.readF4be()) as any
      this.bindingRangeMin0x2c = (this._io.readF4be()) as any
      this.outputValueMax0x30 = (this._io.readF4be()) as any
      this.outputValueMin0x34 = (this._io.readF4be()) as any
      this.value0x38 = (this._io.readF4be()) as any
      this.animationModulationType0x3c = (this._io.readU2be()) as any
      this.bindingModulationType0x3e = (this._io.readU2be()) as any
      this.bindingInvert0x40 = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(3)) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (68) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3067799153) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    binding0xc: GenericGenObject.StringBase;
    cgsResourceHandle0x14: Uint8Array;
    gameChangerId0x1c: number;
    bias0x20: number;
    bindingExponent0x24: number;
    bindingRangeMax0x28: number;
    bindingRangeMin0x2c: number;
    outputValueMax0x30: number;
    outputValueMin0x34: number;
    value0x38: number;

    /**
     * enum; 00_03_f6_5b_1
     */
    animationModulationType0x3c: number;

    /**
     * enum; 00_03_f6_5b_1
     */
    bindingModulationType0x3e: number;
    bindingInvert0x40: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class T0005Ab65 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class T0006Cc72 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class T0006Fa70 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenCameraGameplayShakeEffectTranslation {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.x0xc = (this._io.readU1()) as any
      this.y0x38 = (this._io.readU1()) as any
      this.z0x64 = (this._io.readU1()) as any
      this.gameChangerId0x90 = (this._io.readU4be()) as any
      this.amplitude0x94 = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (152) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (866205257) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;

    /**
     * enum; 00_06_8f_dc_1
     */
    x0xc: number;

    /**
     * enum; 00_06_8f_dc_1
     */
    y0x38: number;

    /**
     * enum; 00_06_8f_dc_1
     */
    z0x64: number;
    gameChangerId0x90: number;
    amplitude0x94: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenEnvironmentKeyframeHeatHaze {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.amplitude0x10 = (this._io.readF4be()) as any
      this.float32T0x14 = (this._io.readF4be()) as any
      this.float32T0x18 = (this._io.readF4be()) as any
      this.frequency0x1c = (this._io.readF4be()) as any
      this.float32T0x20 = (this._io.readF4be()) as any
      this.float32T0x24 = (this._io.readF4be()) as any
      this.float32T0x28 = (this._io.readF4be()) as any
      this.float32T0x2c = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (48) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (4259325714) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    amplitude0x10: number;
    float32T0x14: number;
    float32T0x18: number;
    frequency0x1c: number;
    float32T0x20: number;
    float32T0x24: number;
    float32T0x28: number;
    float32T0x2c: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenUielementPrototypeLabelString {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.binding0xc = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.gameChangerId0x14 = (this._io.readU4be()) as any
      this.cgsCoreUniqueId0x18 = (this._io.readU4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (28) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3798955972) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    binding0xc: GenericGenObject.StringBase;
    gameChangerId0x14: number;
    cgsCoreUniqueId0x18: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenEntitlement {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.description0xc = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.entitlementTag0x14 = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.name0x1c = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.gameChangerId0x24 = (this._io.readU4be()) as any
      this.purchasable0x28 = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(3)) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (44) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2560361681) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    description0xc: GenericGenObject.StringBase;
    entitlementTag0x14: GenericGenObject.StringBase;
    name0x1c: GenericGenObject.StringBase;
    gameChangerId0x24: number;
    purchasable0x28: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenWcvfxBehaviourSpotEffects {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.cgsResourceHandle0xc = (this._io.readBytes(8)) as any
      this.gameChangerId0x14 = (this._io.readU4be()) as any
      this.locatorGroup0x18 = (this._io.readU4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (28) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3960909674) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    cgsResourceHandle0xc: Uint8Array;
    gameChangerId0x14: number;
    locatorGroup0x18: number;
  }
}

export namespace GenericGenObject {
  export class T0005F393 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenUielementPrototypeImageOpacity {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.binding0xc = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.gameChangerId0x14 = (this._io.readU4be()) as any
      this.value0x18 = (this._io.readS4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (28) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1562403887) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    binding0xc: GenericGenObject.StringBase;
    gameChangerId0x14: number;
    value0x18: number;
  }
}

export namespace GenericGenObject {
  export class T00045eF1 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenMixerChannel {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.distanceFalloff0xc = (this._io.readBytes(8)) as any
      this.mixingGroup0x14 = (this._io.readBytes(8)) as any
      this.plugInChain0x1c = (this._io.readBytes(8)) as any
      this.voiceGroup0x24 = (this._io.readBytes(8)) as any
      this.gameChangerId0x2c = (this._io.readU4be()) as any
      this.emitterResponse0x30 = (this._io.readF4be()) as any
      this.focus0x34 = (this._io.readF4be()) as any
      this.gain0x38 = (this._io.readF4be()) as any
      this.lfeSend0x3c = (this._io.readF4be()) as any
      this.panningCosine0x40 = (this._io.readF4be()) as any
      this.panningDivergence0x44 = (this._io.readF4be()) as any
      this.panningSine0x48 = (this._io.readF4be()) as any
      this.reverbSendA0x4c = (this._io.readF4be()) as any
      this.reverbSendB0x50 = (this._io.readF4be()) as any
      this.ptrArrPriority0x54 = (this._io.readU4be()) as any
      this.dopplerModel0x58 = (this._io.readU2be()) as any
      this.arrayCountFor0x54 = (this._io.readU2be()) as any
      this.cullPlayingVoices0x5c = (this._io.readU1()) as any
      this.panningOverride0x5d = (this._io.readU1()) as any
      this.instanceLimit0x5e = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(1)) as any
    }

    private _instPriority0x54: Array<number | undefined> | undefined;
    get instPriority0x54(): Array<number | undefined> | undefined {
      if (typeof this._instPriority0x54 !== 'undefined')
        return this._instPriority0x54;
      if ((this.ptrArrPriority0x54 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrPriority0x54 as any));
        this._instPriority0x54 = [];
        for (let i = 0; i < (this.arrayCountFor0x54 as any); i++) {
          this._instPriority0x54.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._instPriority0x54;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (96) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3718953067) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    distanceFalloff0xc: Uint8Array;
    mixingGroup0x14: Uint8Array;
    plugInChain0x1c: Uint8Array;
    voiceGroup0x24: Uint8Array;
    gameChangerId0x2c: number;
    emitterResponse0x30: number;
    focus0x34: number;
    gain0x38: number;
    lfeSend0x3c: number;
    panningCosine0x40: number;
    panningDivergence0x44: number;
    panningSine0x48: number;
    reverbSendA0x4c: number;
    reverbSendB0x50: number;

    /**
     * enum; 00_07_6b_0e_1
     */
    ptrArrPriority0x54: number;

    /**
     * enum; 00_00_30_22_1
     */
    dopplerModel0x58: number;

    /**
     * "PriorityCount"
     */
    arrayCountFor0x54: number;
    cullPlayingVoices0x5c: number;
    panningOverride0x5d: number;
    instanceLimit0x5e: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenSnapToWorldBehaviour {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenBehaviour(this._io, this, this._root)) as any
      this.distance0x1c = (this._io.readF4be()) as any
      this.float32T0x20 = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (36) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3877549313) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenBehaviour;
    distance0x1c: number;
    float32T0x20: number;
  }
}

export namespace GenericGenObject {
  export class Uint8T {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenUielementPrototypeLabel {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.unkEnum0x10 = (this._io.readU4be()) as any
      this.unkEnum0x14 = (this._io.readU4be()) as any
      this.ptrGenesysGenUielementBase0x18 = (this._io.readU4be()) as any
      this.int32T0x1c = (this._io.readS4be()) as any
      this.bool8T0x20 = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(3)) as any
    }

    private _inst00002a84120x14: number | undefined;
    get inst00002a84120x14(): number | undefined {
      if (typeof this._inst00002a84120x14 !== 'undefined')
        return this._inst00002a84120x14;
      if ((this.unkEnum0x14 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.unkEnum0x14 as any));
        this._inst00002a84120x14 = (this._io.readU4be()) as any
        this._io.seek(_pos);
      }
      return this._inst00002a84120x14;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (36) as any
      return this._size;
    }

    private _inst00002a84110x10: number | undefined;
    get inst00002a84110x10(): number | undefined {
      if (typeof this._inst00002a84110x10 !== 'undefined')
        return this._inst00002a84110x10;
      if ((this.unkEnum0x10 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.unkEnum0x10 as any));
        this._inst00002a84110x10 = (this._io.readU4be()) as any
        this._io.seek(_pos);
      }
      return this._inst00002a84110x10;
    }

    private _instGenesysGenUielementBase0x18: GenericGenObject.GenesysGenUielementBase | undefined;
    get instGenesysGenUielementBase0x18(): GenericGenObject.GenesysGenUielementBase | undefined {
      if (typeof this._instGenesysGenUielementBase0x18 !== 'undefined')
        return this._instGenesysGenUielementBase0x18;
      if ((this.ptrGenesysGenUielementBase0x18 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrGenesysGenUielementBase0x18 as any));
        this._instGenesysGenUielementBase0x18 = (new GenericGenObject.GenesysGenUielementBase(this._io, this, this._root)) as any
        this._io.seek(_pos);
      }
      return this._instGenesysGenUielementBase0x18;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3657730227) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;

    /**
     * enum; 00_00_2a_84_1_1
     */
    unkEnum0x10: number;

    /**
     * enum; 00_00_2a_84_1_2
     */
    unkEnum0x14: number;
    ptrGenesysGenUielementBase0x18: number;
    int32T0x1c: number;
    bool8T0x20: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenEventLocation {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.arrInlinePosition0xc = [];
      for (let i = 0; i < 3; i++) {
        this.arrInlinePosition0xc.push(this._io.readF4be());
      }
      this.eventList0x18 = (this._io.readBytes(8)) as any
      this.mainMapCamera0x20 = (this._io.readBytes(8)) as any
      this.zoomedMapCamera0x28 = (this._io.readBytes(8)) as any
      this.freedriveEvent0x30 = (this._io.readU4be()) as any
      this.gameChangerId0x34 = (this._io.readU4be()) as any
      this.name0x38 = (this._io.readU4be()) as any
      this.originalGamePack0x3c = (this._io.readU4be()) as any
      this.arrayCountFor0xc = (this._io.readU2be()) as any
      this.isCopLocation0x42 = (this._io.readU1()) as any
      this.isOnline0x43 = (this._io.readU1()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (68) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3916132985) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    arrInlinePosition0xc: Array<number>;
    eventList0x18: Uint8Array;
    mainMapCamera0x20: Uint8Array;
    zoomedMapCamera0x28: Uint8Array;
    freedriveEvent0x30: number;
    gameChangerId0x34: number;
    name0x38: number;
    originalGamePack0x3c: number;

    /**
     * "PositionCount"
     */
    arrayCountFor0xc: number;
    isCopLocation0x42: number;
    isOnline0x43: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenMakePhysicalBehaviour {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenBehaviour(this._io, this, this._root)) as any
      this.unkEnum0x1c = (this._io.readU2be()) as any
      this.collidable0x1e = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(1)) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (32) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (477258504) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenBehaviour;

    /**
     * enum; 00_09_37_a3_1
     */
    unkEnum0x1c: number;
    collidable0x1e: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenCameraGameplayShakeEffectTranslationAxisParams {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.amplitude0x10 = (this._io.readF4be()) as any
      this.inwardsDamping0x14 = (this._io.readF4be()) as any
      this.lowerTranslationLimit0x18 = (this._io.readF4be()) as any
      this.outwardsDamping0x1c = (this._io.readF4be()) as any
      this.springCoefficient0x20 = (this._io.readF4be()) as any
      this.upperTranslationLimit0x24 = (this._io.readF4be()) as any
      this.invertForceDirection0x28 = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(3)) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (44) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3529693283) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    amplitude0x10: number;
    inwardsDamping0x14: number;
    lowerTranslationLimit0x18: number;
    outwardsDamping0x1c: number;
    springCoefficient0x20: number;
    upperTranslationLimit0x24: number;
    invertForceDirection0x28: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenUilayoutInstanceParamsTimelineParameters {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.cgsCoreStringBase0xc = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.cgsCoreStringBase0x14 = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.cgsCoreStringBase0x1c = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.cgsCoreStringBase0x24 = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.cgsCoreStringBase0x2c = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.gameChangerId0x34 = (this._io.readU4be()) as any
      this.int32T0x38 = (this._io.readS4be()) as any
      this.triggerType0x3c = (this._io.readU4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (64) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (796059478) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    cgsCoreStringBase0xc: GenericGenObject.StringBase;
    cgsCoreStringBase0x14: GenericGenObject.StringBase;
    cgsCoreStringBase0x1c: GenericGenObject.StringBase;
    cgsCoreStringBase0x24: GenericGenObject.StringBase;
    cgsCoreStringBase0x2c: GenericGenObject.StringBase;
    gameChangerId0x34: number;
    int32T0x38: number;

    /**
     * enum; 00_00_31_b6_1
     */
    triggerType0x3c: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenEnvironmentTimeline {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.unkEnum0x10 = (this._io.readU4be()) as any
      this.arrayCountFor0x10 = (this._io.readU2be()) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _inst000027Df110x10: Array<number | undefined> | undefined;
    get inst000027Df110x10(): Array<number | undefined> | undefined {
      if (typeof this._inst000027Df110x10 !== 'undefined')
        return this._inst000027Df110x10;
      if ((this.unkEnum0x10 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.unkEnum0x10 as any));
        this._inst000027Df110x10 = [];
        for (let i = 0; i < (this.arrayCountFor0x10 as any); i++) {
          this._inst000027Df110x10.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._inst000027Df110x10;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (24) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2446666186) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;

    /**
     * enum; 00_00_27_df_1_1
     */
    unkEnum0x10: number;
    arrayCountFor0x10: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class Uint32T {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class T000733Ee {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenSpikeStripWeapon {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenWeapon(this._io, this, this._root)) as any
      this.rwMathVpuVector30xb0 = (new GenericGenObject.RwMathVpuVector3(this._io, this, this._root)) as any
      this.rwMathVpuVector30xc0 = (new GenericGenObject.RwMathVpuVector3(this._io, this, this._root)) as any
      this.surface0xd0 = (this._io.readU4be()) as any
      this.float32T0xd4 = (this._io.readF4be()) as any
      this.float32T0xd8 = (this._io.readF4be()) as any
      this.float32T0xdc = (this._io.readF4be()) as any
      this.float32T0xe0 = (this._io.readF4be()) as any
      this.float32T0xe4 = (this._io.readF4be()) as any
      this.float32T0xe8 = (this._io.readF4be()) as any
      this.bool8T0xec = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(3)) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (240) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1589479971) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenWeapon;
    rwMathVpuVector30xb0: GenericGenObject.RwMathVpuVector3;
    rwMathVpuVector30xc0: GenericGenObject.RwMathVpuVector3;
    surface0xd0: number;
    float32T0xd4: number;
    float32T0xd8: number;
    float32T0xdc: number;
    float32T0xe0: number;
    float32T0xe4: number;
    float32T0xe8: number;
    bool8T0xec: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenEnvironmentKeyframeCamera {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.rwMathVpuVector40x10 = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
      this.gameChangerId0x20 = (this._io.readU4be()) as any
      this.float32T0x24 = (this._io.readF4be()) as any
      this.float32T0x28 = (this._io.readF4be()) as any
      this.float32T0x2c = (this._io.readF4be()) as any
      this.float32T0x30 = (this._io.readF4be()) as any
      this.float32T0x34 = (this._io.readF4be()) as any
      this.float32T0x38 = (this._io.readF4be()) as any
      this.float32T0x3c = (this._io.readF4be()) as any
      this.float32T0x40 = (this._io.readF4be()) as any
      this.darkBloomWeight0x44 = (this._io.readF4be()) as any
      this.darkBloomWhitePoint0x48 = (this._io.readF4be()) as any
      this.float32T0x4c = (this._io.readF4be()) as any
      this.float32T0x50 = (this._io.readF4be()) as any
      this.float32T0x54 = (this._io.readF4be()) as any
      this.arrInlineFloat32T0x58 = [];
      for (let i = 0; i < 5; i++) {
        this.arrInlineFloat32T0x58.push(this._io.readF4be());
      }
      this.arrInlineFloat32T0x6c = [];
      for (let i = 0; i < 4; i++) {
        this.arrInlineFloat32T0x6c.push(this._io.readF4be());
      }
      this.float32T0x7c = (this._io.readF4be()) as any
      this.arrayCountFor0x58 = (this._io.readU2be()) as any
      this.arrayCountFor0x6c = (this._io.readU2be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (132) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1895175564) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    rwMathVpuVector40x10: GenericGenObject.RwMathVpuVector4;
    gameChangerId0x20: number;
    float32T0x24: number;
    float32T0x28: number;
    float32T0x2c: number;
    float32T0x30: number;
    float32T0x34: number;
    float32T0x38: number;
    float32T0x3c: number;
    float32T0x40: number;
    darkBloomWeight0x44: number;
    darkBloomWhitePoint0x48: number;
    float32T0x4c: number;
    float32T0x50: number;
    float32T0x54: number;
    arrInlineFloat32T0x58: Array<number>;
    arrInlineFloat32T0x6c: Array<number>;
    float32T0x7c: number;
    arrayCountFor0x58: number;
    arrayCountFor0x6c: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenCoronaBeam {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.colour0x10 = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
      this.arrInlineFloat32T0x20 = [];
      for (let i = 0; i < 6; i++) {
        this.arrInlineFloat32T0x20.push(this._io.readF4be());
      }
      this.arrInlineFloat32T0x38 = [];
      for (let i = 0; i < 6; i++) {
        this.arrInlineFloat32T0x38.push(this._io.readF4be());
      }
      this.material0x50 = (this._io.readBytes(8)) as any
      this.gameChangerId0x58 = (this._io.readU4be()) as any
      this.brightness0x5c = (this._io.readF4be()) as any
      this.depthBias0x60 = (this._io.readF4be()) as any
      this.float32T0x64 = (this._io.readF4be()) as any
      this.endRadius0x68 = (this._io.readF4be()) as any
      this.float32T0x6c = (this._io.readF4be()) as any
      this.startRadius0x70 = (this._io.readF4be()) as any
      this.arrayCountFor0x20 = (this._io.readU2be()) as any
      this.arrayCountFor0x38 = (this._io.readU2be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (120) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3046792924) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    colour0x10: GenericGenObject.RwMathVpuVector4;
    arrInlineFloat32T0x20: Array<number>;
    arrInlineFloat32T0x38: Array<number>;
    material0x50: Uint8Array;
    gameChangerId0x58: number;
    brightness0x5c: number;
    depthBias0x60: number;
    float32T0x64: number;
    endRadius0x68: number;
    float32T0x6c: number;
    startRadius0x70: number;
    arrayCountFor0x20: number;
    arrayCountFor0x38: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenRollout {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.arrInlineWeaponData0xc = [];
      for (let i = 0; i < 2; i++) {
        this.arrInlineWeaponData0xc.push(this._io.readU1());
      }
      this.gameChangerId0x44 = (this._io.readU4be()) as any
      this.name0x48 = (this._io.readU4be()) as any
      this.ptrArrCgsCoreUniqueId0x4c = (this._io.readU4be()) as any
      this.cgsCoreUniqueId0x50 = (this._io.readU4be()) as any
      this.vehicle0x54 = (this._io.readU4be()) as any
      this.arrayCountFor0x4c = (this._io.readU2be()) as any
      this.arrayCountFor0xc = (this._io.readU2be()) as any
      this.isOnlineRollout0x5c = (this._io.readU1()) as any
      this.isPlayerRollout0x5d = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _instCgsCoreUniqueId0x4c: Array<number | undefined> | undefined;
    get instCgsCoreUniqueId0x4c(): Array<number | undefined> | undefined {
      if (typeof this._instCgsCoreUniqueId0x4c !== 'undefined')
        return this._instCgsCoreUniqueId0x4c;
      if ((this.ptrArrCgsCoreUniqueId0x4c as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrCgsCoreUniqueId0x4c as any));
        this._instCgsCoreUniqueId0x4c = [];
        for (let i = 0; i < (this.arrayCountFor0x4c as any); i++) {
          this._instCgsCoreUniqueId0x4c.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._instCgsCoreUniqueId0x4c;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (96) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3685564593) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;

    /**
     * enum; 00_04_64_5e_1
     */
    arrInlineWeaponData0xc: Array<number>;
    gameChangerId0x44: number;
    name0x48: number;
    ptrArrCgsCoreUniqueId0x4c: number;
    cgsCoreUniqueId0x50: number;
    vehicle0x54: number;
    arrayCountFor0x4c: number;
    arrayCountFor0xc: number;
    isOnlineRollout0x5c: number;
    isPlayerRollout0x5d: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class T0005F643 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenPostFxKeyframeStereo3d {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.float32T0x10 = (this._io.readF4be()) as any
      this.focusDistance0x14 = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (24) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1324301512) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    float32T0x10: number;
    focusDistance0x14: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenNucleusEntitlementTag {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.tag0xc = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.gameChangerId0x14 = (this._io.readU4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (24) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1212586379) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    tag0xc: GenericGenObject.StringBase;
    gameChangerId0x14: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenUielementElementStackTemplate {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.binding0xc = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.cgsResourceHandle0x14 = (this._io.readBytes(8)) as any
      this.gameChangerId0x1c = (this._io.readU4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (32) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3175993083) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    binding0xc: GenericGenObject.StringBase;
    cgsResourceHandle0x14: Uint8Array;
    gameChangerId0x1c: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenCustomChevron {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.ptrArrFloat32T0x10 = (this._io.readU4be()) as any
      this.ptrArrFloat32T0x14 = (this._io.readU4be()) as any
      this.ptrArrFloat32T0x18 = (this._io.readU4be()) as any
      this.arrayCountFor0x10 = (this._io.readU2be()) as any
      this.arrayCountFor0x14 = (this._io.readU2be()) as any
      this.arrayCountFor0x18 = (this._io.readU2be()) as any
      this.invertNormal0x22 = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(1)) as any
    }

    private _instFloat32T0x14: Array<number | undefined> | undefined;
    get instFloat32T0x14(): Array<number | undefined> | undefined {
      if (typeof this._instFloat32T0x14 !== 'undefined')
        return this._instFloat32T0x14;
      if ((this.ptrArrFloat32T0x14 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrFloat32T0x14 as any));
        this._instFloat32T0x14 = [];
        for (let i = 0; i < (this.arrayCountFor0x14 as any); i++) {
          this._instFloat32T0x14.push(this._io.readF4be());
        }
        this._io.seek(_pos);
      }
      return this._instFloat32T0x14;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (36) as any
      return this._size;
    }

    private _instFloat32T0x10: Array<number | undefined> | undefined;
    get instFloat32T0x10(): Array<number | undefined> | undefined {
      if (typeof this._instFloat32T0x10 !== 'undefined')
        return this._instFloat32T0x10;
      if ((this.ptrArrFloat32T0x10 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrFloat32T0x10 as any));
        this._instFloat32T0x10 = [];
        for (let i = 0; i < (this.arrayCountFor0x10 as any); i++) {
          this._instFloat32T0x10.push(this._io.readF4be());
        }
        this._io.seek(_pos);
      }
      return this._instFloat32T0x10;
    }

    private _instFloat32T0x18: Array<number | undefined> | undefined;
    get instFloat32T0x18(): Array<number | undefined> | undefined {
      if (typeof this._instFloat32T0x18 !== 'undefined')
        return this._instFloat32T0x18;
      if ((this.ptrArrFloat32T0x18 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrFloat32T0x18 as any));
        this._instFloat32T0x18 = [];
        for (let i = 0; i < (this.arrayCountFor0x18 as any); i++) {
          this._instFloat32T0x18.push(this._io.readF4be());
        }
        this._io.seek(_pos);
      }
      return this._instFloat32T0x18;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2896762174) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    ptrArrFloat32T0x10: number;
    ptrArrFloat32T0x14: number;
    ptrArrFloat32T0x18: number;
    arrayCountFor0x10: number;
    arrayCountFor0x14: number;
    arrayCountFor0x18: number;
    invertNormal0x22: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenWaveSequenceItemFade {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.curve0x10 = (this._io.readF4be()) as any
      this.time0x14 = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (24) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2321694493) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    curve0x10: number;
    time0x14: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenVisionMode {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenWeapon(this._io, this, this._root)) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (172) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2653977028) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenWeapon;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenMixingGroup {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.bus0xc = (this._io.readU4be()) as any
      this.gameChangerId0x10 = (this._io.readU4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (20) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (4049496118) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    bus0xc: number;
    gameChangerId0x10: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenPerkLevel {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.description0xc = (this._io.readU4be()) as any
      this.gameChangerId0x10 = (this._io.readU4be()) as any
      this.image0x14 = (this._io.readU4be()) as any
      this.name0x18 = (this._io.readU4be()) as any
      this.ptrArrCgsResourceHandle0x1c = (this._io.readU4be()) as any
      this.arrayCountFor0x1c = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(3)) as any
    }

    private _instCgsResourceHandle0x1c: Array<GenericGenObject.CgsResourceHandle | undefined> | undefined;
    get instCgsResourceHandle0x1c(): Array<GenericGenObject.CgsResourceHandle | undefined> | undefined {
      if (typeof this._instCgsResourceHandle0x1c !== 'undefined')
        return this._instCgsResourceHandle0x1c;
      if ((this.ptrArrCgsResourceHandle0x1c as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrCgsResourceHandle0x1c as any));
        this._instCgsResourceHandle0x1c = [];
        for (let i = 0; i < (this.arrayCountFor0x1c as any); i++) {
          this._instCgsResourceHandle0x1c.push(new GenericGenObject.CgsResourceHandle(this._io, this, this._root));
        }
        this._io.seek(_pos);
      }
      return this._instCgsResourceHandle0x1c;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (36) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1840158847) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    description0xc: number;
    gameChangerId0x10: number;
    image0x14: number;
    name0x18: number;
    ptrArrCgsResourceHandle0x1c: number;
    arrayCountFor0x1c: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenRolloutWeaponData {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.weapon0x10 = (this._io.readU4be()) as any
      this.ptrArrWeaponUpgrades0x14 = (this._io.readU4be()) as any
      this.arrayCountFor0x14 = (this._io.readU2be()) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _instWeaponUpgrades0x14: Array<number | undefined> | undefined;
    get instWeaponUpgrades0x14(): Array<number | undefined> | undefined {
      if (typeof this._instWeaponUpgrades0x14 !== 'undefined')
        return this._instWeaponUpgrades0x14;
      if ((this.ptrArrWeaponUpgrades0x14 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrWeaponUpgrades0x14 as any));
        this._instWeaponUpgrades0x14 = [];
        for (let i = 0; i < (this.arrayCountFor0x14 as any); i++) {
          this._instWeaponUpgrades0x14.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._instWeaponUpgrades0x14;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (28) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3386454351) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    weapon0x10: number;
    ptrArrWeaponUpgrades0x14: number;

    /**
     * "WeaponUpgradesCount"
     */
    arrayCountFor0x14: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenTextStyle {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.cgsCoreUniqueId0xc = (this._io.readU4be()) as any
      this.cgsCoreUniqueId0x10 = (this._io.readU4be()) as any
      this.gameChangerId0x14 = (this._io.readU4be()) as any
      this.cgsCoreUniqueId0x18 = (this._io.readU4be()) as any
      this.float32T0x1c = (this._io.readF4be()) as any
      this.arrInlineFloat32T0x20 = [];
      for (let i = 0; i < 4; i++) {
        this.arrInlineFloat32T0x20.push(this._io.readF4be());
      }
      this.float32T0x30 = (this._io.readF4be()) as any
      this.float32T0x34 = (this._io.readF4be()) as any
      this.arrInlineFloat32T0x38 = [];
      for (let i = 0; i < 4; i++) {
        this.arrInlineFloat32T0x38.push(this._io.readF4be());
      }
      this.float32T0x48 = (this._io.readF4be()) as any
      this.float32T0x4c = (this._io.readF4be()) as any
      this.float32T0x50 = (this._io.readF4be()) as any
      this.float32T0x54 = (this._io.readF4be()) as any
      this.unkEnum0x58 = (this._io.readU4be()) as any
      this.unkEnum0x5c = (this._io.readU2be()) as any
      this.arrayCountFor0x20 = (this._io.readU2be()) as any
      this.arrayCountFor0x38 = (this._io.readU2be()) as any
      this.arrayCountFor0x58 = (this._io.readU2be()) as any
      this.bool8T0x64 = (this._io.readU1()) as any
      this.bool8T0x65 = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _inst00002a58110x58: Array<number | undefined> | undefined;
    get inst00002a58110x58(): Array<number | undefined> | undefined {
      if (typeof this._inst00002a58110x58 !== 'undefined')
        return this._inst00002a58110x58;
      if ((this.unkEnum0x58 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.unkEnum0x58 as any));
        this._inst00002a58110x58 = [];
        for (let i = 0; i < (this.arrayCountFor0x58 as any); i++) {
          this._inst00002a58110x58.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._inst00002a58110x58;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (104) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2006191741) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    cgsCoreUniqueId0xc: number;
    cgsCoreUniqueId0x10: number;
    gameChangerId0x14: number;
    cgsCoreUniqueId0x18: number;
    float32T0x1c: number;
    arrInlineFloat32T0x20: Array<number>;
    float32T0x30: number;
    float32T0x34: number;
    arrInlineFloat32T0x38: Array<number>;
    float32T0x48: number;
    float32T0x4c: number;
    float32T0x50: number;
    float32T0x54: number;

    /**
     * enum; 00_00_2a_58_1_1
     */
    unkEnum0x58: number;

    /**
     * enum; a7_6d_0e_28
     */
    unkEnum0x5c: number;
    arrayCountFor0x20: number;
    arrayCountFor0x38: number;
    arrayCountFor0x58: number;
    bool8T0x64: number;
    bool8T0x65: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenWcplaySoundBehaviour {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenBehaviour(this._io, this, this._root)) as any
      this.offset0x20 = (new GenericGenObject.RwMathVpuVector3(this._io, this, this._root)) as any
      this.mixerChannel0x30 = (this._io.readBytes(8)) as any
      this.ptrArrCgsResourceHandle0x38 = (this._io.readU4be()) as any
      this.ptrArrCgsResourceHandle0x3c = (this._io.readU4be()) as any
      this.ptrArrSurfaceCollisions0x40 = (this._io.readU4be()) as any
      this.arrayCountFor0x38 = (this._io.readU2be()) as any
      this.arrayCountFor0x3c = (this._io.readU2be()) as any
      this.arrayCountFor0x40 = (this._io.readU2be()) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _instSurfaceCollisions0x40: Array<number | undefined> | undefined;
    get instSurfaceCollisions0x40(): Array<number | undefined> | undefined {
      if (typeof this._instSurfaceCollisions0x40 !== 'undefined')
        return this._instSurfaceCollisions0x40;
      if ((this.ptrArrSurfaceCollisions0x40 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrSurfaceCollisions0x40 as any));
        this._instSurfaceCollisions0x40 = [];
        for (let i = 0; i < (this.arrayCountFor0x40 as any); i++) {
          this._instSurfaceCollisions0x40.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._instSurfaceCollisions0x40;
    }

    private _instCgsResourceHandle0x38: Array<GenericGenObject.CgsResourceHandle | undefined> | undefined;
    get instCgsResourceHandle0x38(): Array<GenericGenObject.CgsResourceHandle | undefined> | undefined {
      if (typeof this._instCgsResourceHandle0x38 !== 'undefined')
        return this._instCgsResourceHandle0x38;
      if ((this.ptrArrCgsResourceHandle0x38 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrCgsResourceHandle0x38 as any));
        this._instCgsResourceHandle0x38 = [];
        for (let i = 0; i < (this.arrayCountFor0x38 as any); i++) {
          this._instCgsResourceHandle0x38.push(new GenericGenObject.CgsResourceHandle(this._io, this, this._root));
        }
        this._io.seek(_pos);
      }
      return this._instCgsResourceHandle0x38;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (76) as any
      return this._size;
    }

    private _instCgsResourceHandle0x3c: Array<GenericGenObject.CgsResourceHandle | undefined> | undefined;
    get instCgsResourceHandle0x3c(): Array<GenericGenObject.CgsResourceHandle | undefined> | undefined {
      if (typeof this._instCgsResourceHandle0x3c !== 'undefined')
        return this._instCgsResourceHandle0x3c;
      if ((this.ptrArrCgsResourceHandle0x3c as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrCgsResourceHandle0x3c as any));
        this._instCgsResourceHandle0x3c = [];
        for (let i = 0; i < (this.arrayCountFor0x3c as any); i++) {
          this._instCgsResourceHandle0x3c.push(new GenericGenObject.CgsResourceHandle(this._io, this, this._root));
        }
        this._io.seek(_pos);
      }
      return this._instCgsResourceHandle0x3c;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (4218582003) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenBehaviour;
    offset0x20: GenericGenObject.RwMathVpuVector3;
    mixerChannel0x30: Uint8Array;
    ptrArrCgsResourceHandle0x38: number;
    ptrArrCgsResourceHandle0x3c: number;

    /**
     * enum; 00_04_22_99_1
     */
    ptrArrSurfaceCollisions0x40: number;
    arrayCountFor0x38: number;
    arrayCountFor0x3c: number;
    arrayCountFor0x40: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class RwMathVpuVector3 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.arrInlineElements0x0 = [];
      for (let i = 0; i < 3; i++) {
        this.arrInlineElements0x0.push(this._io.readF4be());
      }
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (4) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2784336371) as any
      return this._muVersionHash;
    }

    arrInlineElements0x0: Array<number>;
  }
}

export namespace GenericGenObject {
  export class GenesysGenUielementScrollableLabelString {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.binding0xc = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.gameChangerId0x14 = (this._io.readU4be()) as any
      this.cgsCoreUniqueId0x18 = (this._io.readU4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (28) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (504799179) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    binding0xc: GenericGenObject.StringBase;
    gameChangerId0x14: number;
    cgsCoreUniqueId0x18: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenScoreViewModel {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.ptrArrScore0x10 = (this._io.readU4be()) as any
      this.arrayCountFor0x10 = (this._io.readU2be()) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _instScore0x10: Array<number | undefined> | undefined;
    get instScore0x10(): Array<number | undefined> | undefined {
      if (typeof this._instScore0x10 !== 'undefined')
        return this._instScore0x10;
      if ((this.ptrArrScore0x10 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrScore0x10 as any));
        this._instScore0x10 = [];
        for (let i = 0; i < (this.arrayCountFor0x10 as any); i++) {
          this._instScore0x10.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._instScore0x10;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (24) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3549903212) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    ptrArrScore0x10: number;

    /**
     * "ScoreCount"
     */
    arrayCountFor0x10: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenPostFxKeyframeDepthOfField {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.float32T0x10 = (this._io.readF4be()) as any
      this.float32T0x14 = (this._io.readF4be()) as any
      this.float32T0x18 = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (28) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1600514099) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    float32T0x10: number;
    float32T0x14: number;
    float32T0x18: number;
  }
}

export namespace GenericGenObject {
  export class PtrTable {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: unknown | undefined,
      readonly _root: GenericGenObject | undefined,
      dtype: string,
      amt: number,
    ) {
      this.dtype = dtype;
      this.amt = amt;

      this._read();
    }

    _read() {
      this.entries = [];
      for (let i = 0; i < (this.amt as any); i++) {
        this.entries.push(new GenericGenObject.Ptr(this._io, this, this._root, (this.dtype as any)));
      }
    }

    entries: Array<GenericGenObject.Ptr>;
    dtype: string;
    amt: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenPostFxKeyframe {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.vignette0x10 = (this._io.readU1()) as any
      this.bloom0x80 = (this._io.readU1()) as any
      this.general0xd0 = (this._io.readU1()) as any
      this.unkEnum0xf4 = (this._io.readU1()) as any
      this.unkEnum0x110 = (this._io.readU1()) as any
      this.gameChangerId0x128 = (this._io.readU4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (300) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1519651292) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;

    /**
     * enum; 00_00_33_12_1
     */
    vignette0x10: number;

    /**
     * enum; 00_00_33_11_1
     */
    bloom0x80: number;

    /**
     * enum; 00_00_33_13_1
     */
    general0xd0: number;

    /**
     * enum; 00_00_33_14_1
     */
    unkEnum0xf4: number;

    /**
     * enum; 00_00_33_15_1
     */
    unkEnum0x110: number;
    gameChangerId0x128: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenEventTriggerSequenceItem {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenSequenceItem(this._io, this, this._root)) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (32) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2519589055) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenSequenceItem;
  }
}

export namespace GenericGenObject {
  export class GenesysGenUilayoutInstanceParams {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.unkEnum0xc = (this._io.readU1()) as any
      this.rotation0x4c = (this._io.readU1()) as any
      this.scale0x74 = (this._io.readU1()) as any
      this.translation0x9c = (this._io.readU1()) as any
      this.cgsCoreStringBase0xc4 = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.cgsCoreStringBase0xcc = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.gameChangerId0xd4 = (this._io.readU4be()) as any
      this.unkEnum0xd8 = (this._io.readU4be()) as any
      this.unkEnum0xdc = (this._io.readU4be()) as any
      this.int32T0xe0 = (this._io.readS4be()) as any
      this.unkEnum0xe4 = (this._io.readU2be()) as any
      this.unkEnum0xe6 = (this._io.readU2be()) as any
      this.arrayCountFor0xdc = (this._io.readU2be()) as any
      this.arrayCountFor0xd8 = (this._io.readU2be()) as any
    }

    private _inst0000337810xd8: Array<number | undefined> | undefined;
    get inst0000337810xd8(): Array<number | undefined> | undefined {
      if (typeof this._inst0000337810xd8 !== 'undefined')
        return this._inst0000337810xd8;
      if ((this.unkEnum0xd8 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.unkEnum0xd8 as any));
        this._inst0000337810xd8 = [];
        for (let i = 0; i < (this.arrayCountFor0xd8 as any); i++) {
          this._inst0000337810xd8.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._inst0000337810xd8;
    }

    private _inst0000337710xdc: Array<number | undefined> | undefined;
    get inst0000337710xdc(): Array<number | undefined> | undefined {
      if (typeof this._inst0000337710xdc !== 'undefined')
        return this._inst0000337710xdc;
      if ((this.unkEnum0xdc as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.unkEnum0xdc as any));
        this._inst0000337710xdc = [];
        for (let i = 0; i < (this.arrayCountFor0xdc as any); i++) {
          this._inst0000337710xdc.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._inst0000337710xdc;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (236) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3550644905) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;

    /**
     * enum; 00_00_33_78_1
     */
    unkEnum0xc: number;

    /**
     * enum; 00_00_33_77_1
     */
    rotation0x4c: number;

    /**
     * enum; 00_00_33_77_1
     */
    scale0x74: number;

    /**
     * enum; 00_00_33_77_1
     */
    translation0x9c: number;
    cgsCoreStringBase0xc4: GenericGenObject.StringBase;
    cgsCoreStringBase0xcc: GenericGenObject.StringBase;
    gameChangerId0xd4: number;

    /**
     * enum; 00_00_33_78_1
     */
    unkEnum0xd8: number;

    /**
     * enum; 00_00_33_77_1
     */
    unkEnum0xdc: number;
    int32T0xe0: number;

    /**
     * enum; 00_00_31_ba_1
     */
    unkEnum0xe4: number;

    /**
     * enum; 00_00_31_c4_1
     */
    unkEnum0xe6: number;
    arrayCountFor0xdc: number;
    arrayCountFor0xd8: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenGameplayTriggerInput {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.ptrArrTrigger0x10 = (this._io.readU4be()) as any
      this.arrayCountFor0x10 = (this._io.readU2be()) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _instTrigger0x10: Array<number | undefined> | undefined;
    get instTrigger0x10(): Array<number | undefined> | undefined {
      if (typeof this._instTrigger0x10 !== 'undefined')
        return this._instTrigger0x10;
      if ((this.ptrArrTrigger0x10 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrTrigger0x10 as any));
        this._instTrigger0x10 = [];
        for (let i = 0; i < (this.arrayCountFor0x10 as any); i++) {
          this._instTrigger0x10.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._instTrigger0x10;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (24) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (934085957) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    ptrArrTrigger0x10: number;
    arrayCountFor0x10: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class RwMathVpuMatrix44affine {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.arrInlineElements0x0 = [];
      for (let i = 0; i < 4; i++) {
        this.arrInlineElements0x0.push(new GenericGenObject.RwMathVpuVector4(this._io, this, this._root));
      }
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (4) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3062587406) as any
      return this._muVersionHash;
    }

    arrInlineElements0x0: Array<GenericGenObject.RwMathVpuVector4>;
  }
}

export namespace GenericGenObject {
  export class GenesysGenOfflineEventCustomChevrons {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.ptrArrFloat32T0x10 = (this._io.readU4be()) as any
      this.ptrArrFloat32T0x14 = (this._io.readU4be()) as any
      this.ptrArrFloat32T0x18 = (this._io.readU4be()) as any
      this.arrayCountFor0x10 = (this._io.readU2be()) as any
      this.arrayCountFor0x14 = (this._io.readU2be()) as any
      this.arrayCountFor0x18 = (this._io.readU2be()) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _instFloat32T0x14: Array<number | undefined> | undefined;
    get instFloat32T0x14(): Array<number | undefined> | undefined {
      if (typeof this._instFloat32T0x14 !== 'undefined')
        return this._instFloat32T0x14;
      if ((this.ptrArrFloat32T0x14 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrFloat32T0x14 as any));
        this._instFloat32T0x14 = [];
        for (let i = 0; i < (this.arrayCountFor0x14 as any); i++) {
          this._instFloat32T0x14.push(this._io.readF4be());
        }
        this._io.seek(_pos);
      }
      return this._instFloat32T0x14;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (36) as any
      return this._size;
    }

    private _instFloat32T0x10: Array<number | undefined> | undefined;
    get instFloat32T0x10(): Array<number | undefined> | undefined {
      if (typeof this._instFloat32T0x10 !== 'undefined')
        return this._instFloat32T0x10;
      if ((this.ptrArrFloat32T0x10 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrFloat32T0x10 as any));
        this._instFloat32T0x10 = [];
        for (let i = 0; i < (this.arrayCountFor0x10 as any); i++) {
          this._instFloat32T0x10.push(this._io.readF4be());
        }
        this._io.seek(_pos);
      }
      return this._instFloat32T0x10;
    }

    private _instFloat32T0x18: Array<number | undefined> | undefined;
    get instFloat32T0x18(): Array<number | undefined> | undefined {
      if (typeof this._instFloat32T0x18 !== 'undefined')
        return this._instFloat32T0x18;
      if ((this.ptrArrFloat32T0x18 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrFloat32T0x18 as any));
        this._instFloat32T0x18 = [];
        for (let i = 0; i < (this.arrayCountFor0x18 as any); i++) {
          this._instFloat32T0x18.push(this._io.readF4be());
        }
        this._io.seek(_pos);
      }
      return this._instFloat32T0x18;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1721661981) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    ptrArrFloat32T0x10: number;
    ptrArrFloat32T0x14: number;
    ptrArrFloat32T0x18: number;
    arrayCountFor0x10: number;
    arrayCountFor0x14: number;
    arrayCountFor0x18: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class Float32T {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenUielementBase {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.cgsCoreStringBase0xc = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.cgsCoreStringBase0x14 = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.cgsCoreStringBase0x1c = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.cgsCoreStringBase0x24 = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.cgsCoreStringBase0x2c = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.cgsCoreStringBase0x34 = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.cgsCoreStringBase0x3c = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.cgsCoreStringBase0x44 = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.material0x4c = (this._io.readBytes(8)) as any
      this.gameChangerId0x54 = (this._io.readU4be()) as any
      this.ptrArrCgsCoreUniqueId0x58 = (this._io.readU4be()) as any
      this.cgsCoreUniqueId0x5c = (this._io.readU4be()) as any
      this.cgsCoreUniqueId0x60 = (this._io.readU4be()) as any
      this.ptrArrCgsResourceHandle0x64 = (this._io.readU4be()) as any
      this.ptrArrGenesysGenUielementBaseBehaviour0x68 = (this._io.readU4be()) as any
      this.ptrArrGenesysGenUielementBaseBehaviour0x6c = (this._io.readU4be()) as any
      this.ptrArrGenesysGenUielementBaseBehaviour0x70 = (this._io.readU4be()) as any
      this.ptrArrGenesysGenUielementBaseEffectConstant0x74 = (this._io.readU4be()) as any
      this.ptrGenesysGenUielementBaseRenderingData0x78 = (this._io.readU4be()) as any
      this.ptrArrGenesysGenUielementBaseTimeline0x7c = (this._io.readU4be()) as any
      this.int32T0x80 = (this._io.readS4be()) as any
      this.positionX0x84 = (this._io.readS4be()) as any
      this.positionY0x88 = (this._io.readS4be()) as any
      this.rotation0x8c = (this._io.readS4be()) as any
      this.int32T0x90 = (this._io.readS4be()) as any
      this.int32T0x94 = (this._io.readS4be()) as any
      this.int32T0x98 = (this._io.readS4be()) as any
      this.int32T0x9c = (this._io.readS4be()) as any
      this.unkEnum0xa0 = (this._io.readU2be()) as any
      this.arrayCountFor0x74 = (this._io.readU2be()) as any
      this.arrayCountFor0x64 = (this._io.readU2be()) as any
      this.arrayCountFor0x68 = (this._io.readU2be()) as any
      this.arrayCountFor0x58 = (this._io.readU2be()) as any
      this.arrayCountFor0x7c = (this._io.readU2be()) as any
      this.arrayCountFor0x6c = (this._io.readU2be()) as any
      this.arrayCountFor0x70 = (this._io.readU2be()) as any
    }

    private _instCgsResourceHandle0x64: Array<GenericGenObject.CgsResourceHandle | undefined> | undefined;
    get instCgsResourceHandle0x64(): Array<GenericGenObject.CgsResourceHandle | undefined> | undefined {
      if (typeof this._instCgsResourceHandle0x64 !== 'undefined')
        return this._instCgsResourceHandle0x64;
      if ((this.ptrArrCgsResourceHandle0x64 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrCgsResourceHandle0x64 as any));
        this._instCgsResourceHandle0x64 = [];
        for (let i = 0; i < (this.arrayCountFor0x64 as any); i++) {
          this._instCgsResourceHandle0x64.push(new GenericGenObject.CgsResourceHandle(this._io, this, this._root));
        }
        this._io.seek(_pos);
      }
      return this._instCgsResourceHandle0x64;
    }

    private _instGenesysGenUielementBaseTimeline0x7c: Array<GenericGenObject.GenesysGenUielementBaseTimeline | undefined> | undefined;
    get instGenesysGenUielementBaseTimeline0x7c(): Array<GenericGenObject.GenesysGenUielementBaseTimeline | undefined> | undefined {
      if (typeof this._instGenesysGenUielementBaseTimeline0x7c !== 'undefined')
        return this._instGenesysGenUielementBaseTimeline0x7c;
      if ((this.ptrArrGenesysGenUielementBaseTimeline0x7c as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrGenesysGenUielementBaseTimeline0x7c as any));
        this._instGenesysGenUielementBaseTimeline0x7c = [];
        for (let i = 0; i < (this.arrayCountFor0x7c as any); i++) {
          this._instGenesysGenUielementBaseTimeline0x7c.push(new GenericGenObject.GenesysGenUielementBaseTimeline(this._io, this, this._root));
        }
        this._io.seek(_pos);
      }
      return this._instGenesysGenUielementBaseTimeline0x7c;
    }

    private _instGenesysGenUielementBaseBehaviour0x6c: Array<GenericGenObject.GenesysGenUielementBaseBehaviour | undefined> | undefined;
    get instGenesysGenUielementBaseBehaviour0x6c(): Array<GenericGenObject.GenesysGenUielementBaseBehaviour | undefined> | undefined {
      if (typeof this._instGenesysGenUielementBaseBehaviour0x6c !== 'undefined')
        return this._instGenesysGenUielementBaseBehaviour0x6c;
      if ((this.ptrArrGenesysGenUielementBaseBehaviour0x6c as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrGenesysGenUielementBaseBehaviour0x6c as any));
        this._instGenesysGenUielementBaseBehaviour0x6c = [];
        for (let i = 0; i < (this.arrayCountFor0x6c as any); i++) {
          this._instGenesysGenUielementBaseBehaviour0x6c.push(new GenericGenObject.GenesysGenUielementBaseBehaviour(this._io, this, this._root));
        }
        this._io.seek(_pos);
      }
      return this._instGenesysGenUielementBaseBehaviour0x6c;
    }

    private _instGenesysGenUielementBaseRenderingData0x78: GenericGenObject.GenesysGenUielementBaseRenderingData | undefined;
    get instGenesysGenUielementBaseRenderingData0x78(): GenericGenObject.GenesysGenUielementBaseRenderingData | undefined {
      if (typeof this._instGenesysGenUielementBaseRenderingData0x78 !== 'undefined')
        return this._instGenesysGenUielementBaseRenderingData0x78;
      if ((this.ptrGenesysGenUielementBaseRenderingData0x78 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrGenesysGenUielementBaseRenderingData0x78 as any));
        this._instGenesysGenUielementBaseRenderingData0x78 = (new GenericGenObject.GenesysGenUielementBaseRenderingData(this._io, this, this._root)) as any
        this._io.seek(_pos);
      }
      return this._instGenesysGenUielementBaseRenderingData0x78;
    }

    private _instGenesysGenUielementBaseBehaviour0x68: Array<GenericGenObject.GenesysGenUielementBaseBehaviour | undefined> | undefined;
    get instGenesysGenUielementBaseBehaviour0x68(): Array<GenericGenObject.GenesysGenUielementBaseBehaviour | undefined> | undefined {
      if (typeof this._instGenesysGenUielementBaseBehaviour0x68 !== 'undefined')
        return this._instGenesysGenUielementBaseBehaviour0x68;
      if ((this.ptrArrGenesysGenUielementBaseBehaviour0x68 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrGenesysGenUielementBaseBehaviour0x68 as any));
        this._instGenesysGenUielementBaseBehaviour0x68 = [];
        for (let i = 0; i < (this.arrayCountFor0x68 as any); i++) {
          this._instGenesysGenUielementBaseBehaviour0x68.push(new GenericGenObject.GenesysGenUielementBaseBehaviour(this._io, this, this._root));
        }
        this._io.seek(_pos);
      }
      return this._instGenesysGenUielementBaseBehaviour0x68;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (176) as any
      return this._size;
    }

    private _instCgsCoreUniqueId0x58: Array<number | undefined> | undefined;
    get instCgsCoreUniqueId0x58(): Array<number | undefined> | undefined {
      if (typeof this._instCgsCoreUniqueId0x58 !== 'undefined')
        return this._instCgsCoreUniqueId0x58;
      if ((this.ptrArrCgsCoreUniqueId0x58 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrCgsCoreUniqueId0x58 as any));
        this._instCgsCoreUniqueId0x58 = [];
        for (let i = 0; i < (this.arrayCountFor0x58 as any); i++) {
          this._instCgsCoreUniqueId0x58.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._instCgsCoreUniqueId0x58;
    }

    private _instGenesysGenUielementBaseEffectConstant0x74: Array<GenericGenObject.GenesysGenUielementBaseEffectConstant | undefined> | undefined;
    get instGenesysGenUielementBaseEffectConstant0x74(): Array<GenericGenObject.GenesysGenUielementBaseEffectConstant | undefined> | undefined {
      if (typeof this._instGenesysGenUielementBaseEffectConstant0x74 !== 'undefined')
        return this._instGenesysGenUielementBaseEffectConstant0x74;
      if ((this.ptrArrGenesysGenUielementBaseEffectConstant0x74 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrGenesysGenUielementBaseEffectConstant0x74 as any));
        this._instGenesysGenUielementBaseEffectConstant0x74 = [];
        for (let i = 0; i < (this.arrayCountFor0x74 as any); i++) {
          this._instGenesysGenUielementBaseEffectConstant0x74.push(new GenericGenObject.GenesysGenUielementBaseEffectConstant(this._io, this, this._root));
        }
        this._io.seek(_pos);
      }
      return this._instGenesysGenUielementBaseEffectConstant0x74;
    }

    private _instGenesysGenUielementBaseBehaviour0x70: Array<GenericGenObject.GenesysGenUielementBaseBehaviour | undefined> | undefined;
    get instGenesysGenUielementBaseBehaviour0x70(): Array<GenericGenObject.GenesysGenUielementBaseBehaviour | undefined> | undefined {
      if (typeof this._instGenesysGenUielementBaseBehaviour0x70 !== 'undefined')
        return this._instGenesysGenUielementBaseBehaviour0x70;
      if ((this.ptrArrGenesysGenUielementBaseBehaviour0x70 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrGenesysGenUielementBaseBehaviour0x70 as any));
        this._instGenesysGenUielementBaseBehaviour0x70 = [];
        for (let i = 0; i < (this.arrayCountFor0x70 as any); i++) {
          this._instGenesysGenUielementBaseBehaviour0x70.push(new GenericGenObject.GenesysGenUielementBaseBehaviour(this._io, this, this._root));
        }
        this._io.seek(_pos);
      }
      return this._instGenesysGenUielementBaseBehaviour0x70;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3784314544) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    cgsCoreStringBase0xc: GenericGenObject.StringBase;
    cgsCoreStringBase0x14: GenericGenObject.StringBase;
    cgsCoreStringBase0x1c: GenericGenObject.StringBase;
    cgsCoreStringBase0x24: GenericGenObject.StringBase;
    cgsCoreStringBase0x2c: GenericGenObject.StringBase;
    cgsCoreStringBase0x34: GenericGenObject.StringBase;
    cgsCoreStringBase0x3c: GenericGenObject.StringBase;
    cgsCoreStringBase0x44: GenericGenObject.StringBase;
    material0x4c: Uint8Array;
    gameChangerId0x54: number;
    ptrArrCgsCoreUniqueId0x58: number;
    cgsCoreUniqueId0x5c: number;
    cgsCoreUniqueId0x60: number;
    ptrArrCgsResourceHandle0x64: number;
    ptrArrGenesysGenUielementBaseBehaviour0x68: number;
    ptrArrGenesysGenUielementBaseBehaviour0x6c: number;
    ptrArrGenesysGenUielementBaseBehaviour0x70: number;
    ptrArrGenesysGenUielementBaseEffectConstant0x74: number;
    ptrGenesysGenUielementBaseRenderingData0x78: number;
    ptrArrGenesysGenUielementBaseTimeline0x7c: number;
    int32T0x80: number;
    positionX0x84: number;
    positionY0x88: number;
    rotation0x8c: number;
    int32T0x90: number;
    int32T0x94: number;
    int32T0x98: number;
    int32T0x9c: number;

    /**
     * enum; da_dc_9b_17
     */
    unkEnum0xa0: number;
    arrayCountFor0x74: number;
    arrayCountFor0x64: number;
    arrayCountFor0x68: number;
    arrayCountFor0x58: number;
    arrayCountFor0x7c: number;
    arrayCountFor0x6c: number;
    arrayCountFor0x70: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenBusMixerChannelSequenceItem {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenSequenceItem(this._io, this, this._root)) as any
      this.bus0x20 = (this._io.readU4be()) as any
      this.ptrArrAutomatedValues0x24 = (this._io.readU4be()) as any
      this.arrayCountFor0x24 = (this._io.readU2be()) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _instAutomatedValues0x24: Array<number | undefined> | undefined;
    get instAutomatedValues0x24(): Array<number | undefined> | undefined {
      if (typeof this._instAutomatedValues0x24 !== 'undefined')
        return this._instAutomatedValues0x24;
      if ((this.ptrArrAutomatedValues0x24 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrAutomatedValues0x24 as any));
        this._instAutomatedValues0x24 = [];
        for (let i = 0; i < (this.arrayCountFor0x24 as any); i++) {
          this._instAutomatedValues0x24.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._instAutomatedValues0x24;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (44) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3513065817) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenSequenceItem;
    bus0x20: number;

    /**
     * enum; 00_03_f6_d4_1
     */
    ptrArrAutomatedValues0x24: number;

    /**
     * "Automated_ValuesCount"
     */
    arrayCountFor0x24: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenPerformanceUpgradePackage {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenUpgradePackage(this._io, this, this._root)) as any
      this.cgsCoreUniqueId0x1c = (this._io.readU4be()) as any
      this.float32T0x20 = (this._io.readF4be()) as any
      this.unkEnum0x24 = (this._io.readU4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (40) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (546410997) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenUpgradePackage;
    cgsCoreUniqueId0x1c: number;
    float32T0x20: number;

    /**
     * enum; 00_04_5f_b1_1
     */
    unkEnum0x24: number;
  }
}

export namespace GenericGenObject {
  export class GenObj {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.dynamicGamedata = (this._io.readBytes(8)) as any
      this.muTypeVersion = (this._io.readU4le()) as any
    }

    dynamicGamedata: Uint8Array;
    muTypeVersion: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenOfflineEvent {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenEvent(this._io, this, this._root)) as any
      this.cgsCoreUniqueId0x30 = (this._io.readU4be()) as any
      this.cgsCoreUniqueId0x34 = (this._io.readU4be()) as any
      this.ptrArrCgsCoreUniqueId0x38 = (this._io.readU4be()) as any
      this.ptrArrCheckpoints0x3c = (this._io.readU4be()) as any
      this.ptrArrGameplayTriggers0x40 = (this._io.readU4be()) as any
      this.intro0x44 = (this._io.readU4be()) as any
      this.name0x48 = (this._io.readU4be()) as any
      this.nextStoryEvent0x4c = (this._io.readU4be()) as any
      this.deallocatedNodule0x50 = (this._io.readU4be()) as any
      this.ptrArrCgsCoreUniqueId0x54 = (this._io.readU4be()) as any
      this.cgsCoreUniqueId0x58 = (this._io.readU4be()) as any
      this.timeline0x5c = (this._io.readU4be()) as any
      this.ptrArrFloat32T0x60 = (this._io.readU4be()) as any
      this.ptrArrTargetTime0x64 = (this._io.readU4be()) as any
      this.trafficDensity0x68 = (this._io.readF4be()) as any
      this.ptrArrPtrAiplayers0x6c = (this._io.readU4be()) as any
      this.ptrArrPtrChevronList0x70 = (this._io.readU4be()) as any
      this.ptrArrPtrCustomChevronList0x74 = (this._io.readU4be()) as any
      this.targetScore0x78 = (this._io.readU4be()) as any
      this.arrayCountFor0x38 = (this._io.readU2be()) as any
      this.arrayCountFor0x3c = (this._io.readU2be()) as any
      this.arrayCountFor0x70 = (this._io.readU2be()) as any
      this.arrayCountFor0x54 = (this._io.readU2be()) as any
      this.arrayCountFor0x60 = (this._io.readU2be()) as any
      this.arrayCountFor0x64 = (this._io.readU2be()) as any
      this.copSpawning0x88 = (this._io.readU1()) as any
      this.startWithEngineOn0x89 = (this._io.readU1()) as any
      this.trafficEnabled0x8a = (this._io.readU1()) as any
      this.arrayCountFor0x6c = (this._io.readU1()) as any
      this.arrayCountFor0x74 = (this._io.readU1()) as any
      this.arrayCountFor0x40 = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _instGameplayTriggers0x40: Array<number | undefined> | undefined;
    get instGameplayTriggers0x40(): Array<number | undefined> | undefined {
      if (typeof this._instGameplayTriggers0x40 !== 'undefined')
        return this._instGameplayTriggers0x40;
      if ((this.ptrArrGameplayTriggers0x40 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrGameplayTriggers0x40 as any));
        this._instGameplayTriggers0x40 = [];
        for (let i = 0; i < (this.arrayCountFor0x40 as any); i++) {
          this._instGameplayTriggers0x40.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._instGameplayTriggers0x40;
    }

    private _instCgsCoreUniqueId0x54: Array<number | undefined> | undefined;
    get instCgsCoreUniqueId0x54(): Array<number | undefined> | undefined {
      if (typeof this._instCgsCoreUniqueId0x54 !== 'undefined')
        return this._instCgsCoreUniqueId0x54;
      if ((this.ptrArrCgsCoreUniqueId0x54 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrCgsCoreUniqueId0x54 as any));
        this._instCgsCoreUniqueId0x54 = [];
        for (let i = 0; i < (this.arrayCountFor0x54 as any); i++) {
          this._instCgsCoreUniqueId0x54.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._instCgsCoreUniqueId0x54;
    }

    private _instFloat32T0x60: Array<number | undefined> | undefined;
    get instFloat32T0x60(): Array<number | undefined> | undefined {
      if (typeof this._instFloat32T0x60 !== 'undefined')
        return this._instFloat32T0x60;
      if ((this.ptrArrFloat32T0x60 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrFloat32T0x60 as any));
        this._instFloat32T0x60 = [];
        for (let i = 0; i < (this.arrayCountFor0x60 as any); i++) {
          this._instFloat32T0x60.push(this._io.readF4be());
        }
        this._io.seek(_pos);
      }
      return this._instFloat32T0x60;
    }

    private _instCheckpoints0x3c: Array<number | undefined> | undefined;
    get instCheckpoints0x3c(): Array<number | undefined> | undefined {
      if (typeof this._instCheckpoints0x3c !== 'undefined')
        return this._instCheckpoints0x3c;
      if ((this.ptrArrCheckpoints0x3c as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrCheckpoints0x3c as any));
        this._instCheckpoints0x3c = [];
        for (let i = 0; i < (this.arrayCountFor0x3c as any); i++) {
          this._instCheckpoints0x3c.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._instCheckpoints0x3c;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (144) as any
      return this._size;
    }

    private _instChevronList0x70: Array<GenericGenObject.Ptr | undefined> | undefined;
    get instChevronList0x70(): Array<GenericGenObject.Ptr | undefined> | undefined {
      if (typeof this._instChevronList0x70 !== 'undefined')
        return this._instChevronList0x70;
      if ((this.ptrArrPtrChevronList0x70 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrPtrChevronList0x70 as any));
        this._instChevronList0x70 = [];
        for (let i = 0; i < (this.arrayCountFor0x70 as any); i++) {
          this._instChevronList0x70.push(new GenericGenObject.Ptr(this._io, this, this._root, "u4"));
        }
        this._io.seek(_pos);
      }
      return this._instChevronList0x70;
    }

    private _instCgsCoreUniqueId0x38: Array<number | undefined> | undefined;
    get instCgsCoreUniqueId0x38(): Array<number | undefined> | undefined {
      if (typeof this._instCgsCoreUniqueId0x38 !== 'undefined')
        return this._instCgsCoreUniqueId0x38;
      if ((this.ptrArrCgsCoreUniqueId0x38 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrCgsCoreUniqueId0x38 as any));
        this._instCgsCoreUniqueId0x38 = [];
        for (let i = 0; i < (this.arrayCountFor0x38 as any); i++) {
          this._instCgsCoreUniqueId0x38.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._instCgsCoreUniqueId0x38;
    }

    private _instTargetTime0x64: Array<number | undefined> | undefined;
    get instTargetTime0x64(): Array<number | undefined> | undefined {
      if (typeof this._instTargetTime0x64 !== 'undefined')
        return this._instTargetTime0x64;
      if ((this.ptrArrTargetTime0x64 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrTargetTime0x64 as any));
        this._instTargetTime0x64 = [];
        for (let i = 0; i < (this.arrayCountFor0x64 as any); i++) {
          this._instTargetTime0x64.push(this._io.readF4be());
        }
        this._io.seek(_pos);
      }
      return this._instTargetTime0x64;
    }

    private _instCustomChevronList0x74: Array<GenericGenObject.Ptr | undefined> | undefined;
    get instCustomChevronList0x74(): Array<GenericGenObject.Ptr | undefined> | undefined {
      if (typeof this._instCustomChevronList0x74 !== 'undefined')
        return this._instCustomChevronList0x74;
      if ((this.ptrArrPtrCustomChevronList0x74 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrPtrCustomChevronList0x74 as any));
        this._instCustomChevronList0x74 = [];
        for (let i = 0; i < (this.arrayCountFor0x74 as any); i++) {
          this._instCustomChevronList0x74.push(new GenericGenObject.Ptr(this._io, this, this._root, "u4"));
        }
        this._io.seek(_pos);
      }
      return this._instCustomChevronList0x74;
    }

    private _instAiplayers0x6c: Array<GenericGenObject.Ptr | undefined> | undefined;
    get instAiplayers0x6c(): Array<GenericGenObject.Ptr | undefined> | undefined {
      if (typeof this._instAiplayers0x6c !== 'undefined')
        return this._instAiplayers0x6c;
      if ((this.ptrArrPtrAiplayers0x6c as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrPtrAiplayers0x6c as any));
        this._instAiplayers0x6c = [];
        for (let i = 0; i < (this.arrayCountFor0x6c as any); i++) {
          this._instAiplayers0x6c.push(new GenericGenObject.Ptr(this._io, this, this._root, "u4"));
        }
        this._io.seek(_pos);
      }
      return this._instAiplayers0x6c;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (503737009) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenEvent;
    cgsCoreUniqueId0x30: number;
    cgsCoreUniqueId0x34: number;
    ptrArrCgsCoreUniqueId0x38: number;
    ptrArrCheckpoints0x3c: number;
    ptrArrGameplayTriggers0x40: number;
    intro0x44: number;
    name0x48: number;
    nextStoryEvent0x4c: number;
    deallocatedNodule0x50: number;
    ptrArrCgsCoreUniqueId0x54: number;
    cgsCoreUniqueId0x58: number;
    timeline0x5c: number;
    ptrArrFloat32T0x60: number;
    ptrArrTargetTime0x64: number;
    trafficDensity0x68: number;

    /**
     * enum; 00_06_fa_75_1
     */
    ptrArrPtrAiplayers0x6c: number;

    /**
     * enum; 00_04_62_44_1
     */
    ptrArrPtrChevronList0x70: number;

    /**
     * enum; 00_06_fa_9f_1
     */
    ptrArrPtrCustomChevronList0x74: number;
    targetScore0x78: number;
    arrayCountFor0x38: number;

    /**
     * "CheckpointsCount"
     */
    arrayCountFor0x3c: number;

    /**
     * "ChevronListCount"
     */
    arrayCountFor0x70: number;
    arrayCountFor0x54: number;
    arrayCountFor0x60: number;

    /**
     * "TargetTimeCount"
     */
    arrayCountFor0x64: number;
    copSpawning0x88: number;
    startWithEngineOn0x89: number;
    trafficEnabled0x8a: number;

    /**
     * "AIPlayersCount"
     */
    arrayCountFor0x6c: number;

    /**
     * "CustomChevronListCount"
     */
    arrayCountFor0x74: number;

    /**
     * "GameplayTriggersCount"
     */
    arrayCountFor0x40: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class T000031B6 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class Char {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class Dummy {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

    private _d: string;
    get d(): string {
      if (typeof this._d !== 'undefined')
        return this._d;
      this._d = ("dummy") as any
      return this._d;
    }

  }
}

export namespace GenericGenObject {
  export class T06A964Cd {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenFlashHeadlightsWeapon {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenWeapon(this._io, this, this._root)) as any
      this.float32T0xb0 = (this._io.readF4be()) as any
      this.float32T0xb4 = (this._io.readF4be()) as any
      this.float32T0xb8 = (this._io.readF4be()) as any
      this.float32T0xbc = (this._io.readF4be()) as any
      this.float32T0xc0 = (this._io.readF4be()) as any
      this.float32T0xc4 = (this._io.readF4be()) as any
      this.float32T0xc8 = (this._io.readF4be()) as any
      this.float32T0xcc = (this._io.readF4be()) as any
      this.float32T0xd0 = (this._io.readF4be()) as any
      this.float32T0xd4 = (this._io.readF4be()) as any
      this.float32T0xd8 = (this._io.readF4be()) as any
      this.float32T0xdc = (this._io.readF4be()) as any
      this.float32T0xe0 = (this._io.readF4be()) as any
      this.float32T0xe4 = (this._io.readF4be()) as any
      this.float32T0xe8 = (this._io.readF4be()) as any
      this.float32T0xec = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (240) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3376466135) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenWeapon;
    float32T0xb0: number;
    float32T0xb4: number;
    float32T0xb8: number;
    float32T0xbc: number;
    float32T0xc0: number;
    float32T0xc4: number;
    float32T0xc8: number;
    float32T0xcc: number;
    float32T0xd0: number;
    float32T0xd4: number;
    float32T0xd8: number;
    float32T0xdc: number;
    float32T0xe0: number;
    float32T0xe4: number;
    float32T0xe8: number;
    float32T0xec: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenSequence {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.binding0xc = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.gameChangerId0x14 = (this._io.readU4be()) as any
      this.ptrArrSequenceItems0x18 = (this._io.readU4be()) as any
      this.ptrArrTimelineControllers0x1c = (this._io.readU4be()) as any
      this.bindingMax0x20 = (this._io.readF4be()) as any
      this.bindingMin0x24 = (this._io.readF4be()) as any
      this.defaultProgressionController0x28 = (this._io.readU2be()) as any
      this.arrayCountFor0x18 = (this._io.readU2be()) as any
      this.arrayCountFor0x1c = (this._io.readU2be()) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _instSequenceItems0x18: Array<GenericGenObject.CgsResourceHandle | undefined> | undefined;
    get instSequenceItems0x18(): Array<GenericGenObject.CgsResourceHandle | undefined> | undefined {
      if (typeof this._instSequenceItems0x18 !== 'undefined')
        return this._instSequenceItems0x18;
      if ((this.ptrArrSequenceItems0x18 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrSequenceItems0x18 as any));
        this._instSequenceItems0x18 = [];
        for (let i = 0; i < (this.arrayCountFor0x18 as any); i++) {
          this._instSequenceItems0x18.push(new GenericGenObject.CgsResourceHandle(this._io, this, this._root));
        }
        this._io.seek(_pos);
      }
      return this._instSequenceItems0x18;
    }

    private _instTimelineControllers0x1c: Array<GenericGenObject.CgsResourceHandle | undefined> | undefined;
    get instTimelineControllers0x1c(): Array<GenericGenObject.CgsResourceHandle | undefined> | undefined {
      if (typeof this._instTimelineControllers0x1c !== 'undefined')
        return this._instTimelineControllers0x1c;
      if ((this.ptrArrTimelineControllers0x1c as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrTimelineControllers0x1c as any));
        this._instTimelineControllers0x1c = [];
        for (let i = 0; i < (this.arrayCountFor0x1c as any); i++) {
          this._instTimelineControllers0x1c.push(new GenericGenObject.CgsResourceHandle(this._io, this, this._root));
        }
        this._io.seek(_pos);
      }
      return this._instTimelineControllers0x1c;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (48) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (4243611625) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    binding0xc: GenericGenObject.StringBase;
    gameChangerId0x14: number;
    ptrArrSequenceItems0x18: number;
    ptrArrTimelineControllers0x1c: number;
    bindingMax0x20: number;
    bindingMin0x24: number;

    /**
     * enum; 00_03_f6_83_1
     */
    defaultProgressionController0x28: number;

    /**
     * "SequenceItemsCount"
     */
    arrayCountFor0x18: number;

    /**
     * "TimelineControllersCount"
     */
    arrayCountFor0x1c: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenPostFxstate {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.arrInlineColourCubes0xc = [];
      for (let i = 0; i < 2; i++) {
        this.arrInlineColourCubes0xc.push(this._io.readU1());
      }
      this.bloomValueModification0x44 = (this._io.readU1()) as any
      this.colourCubeValueModification0x5c = (this._io.readU1()) as any
      this.dofValueModification0x74 = (this._io.readU1()) as any
      this.generalValueModification0x8c = (this._io.readU1()) as any
      this.vignetteValueModification0xa4 = (this._io.readU1()) as any
      this.activityBinding0xbc = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.keyframeBlendBinding0xc4 = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.valueBinding0xcc = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.keyFrame10xd4 = (this._io.readBytes(8)) as any
      this.keyFrame20xdc = (this._io.readBytes(8)) as any
      this.gameChangerId0xe4 = (this._io.readU4be()) as any
      this.rateOfChange0xe8 = (this._io.readF4be()) as any
      this.value0xec = (this._io.readF4be()) as any
      this.changeBehaviour0xf0 = (this._io.readU2be()) as any
      this.arrayCountFor0xc = (this._io.readU2be()) as any
      this.useBloom0xf4 = (this._io.readU1()) as any
      this.useDof0xf5 = (this._io.readU1()) as any
      this.useGeneralFx0xf6 = (this._io.readU1()) as any
      this.useVignette0xf7 = (this._io.readU1()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (248) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (615742248) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;

    /**
     * enum; 00_00_33_16_1
     */
    arrInlineColourCubes0xc: Array<number>;

    /**
     * enum; 00_00_33_17_1
     */
    bloomValueModification0x44: number;

    /**
     * enum; 00_00_33_17_1
     */
    colourCubeValueModification0x5c: number;

    /**
     * enum; 00_00_33_17_1
     */
    dofValueModification0x74: number;

    /**
     * enum; 00_00_33_17_1
     */
    generalValueModification0x8c: number;

    /**
     * enum; 00_00_33_17_1
     */
    vignetteValueModification0xa4: number;
    activityBinding0xbc: GenericGenObject.StringBase;
    keyframeBlendBinding0xc4: GenericGenObject.StringBase;
    valueBinding0xcc: GenericGenObject.StringBase;
    keyFrame10xd4: Uint8Array;
    keyFrame20xdc: Uint8Array;
    gameChangerId0xe4: number;
    rateOfChange0xe8: number;
    value0xec: number;

    /**
     * enum; 00_00_30_38_1
     */
    changeBehaviour0xf0: number;

    /**
     * "ColourCubesCount"
     */
    arrayCountFor0xc: number;
    useBloom0xf4: number;
    useDof0xf5: number;
    useGeneralFx0xf6: number;
    useVignette0xf7: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenUielementElementStack {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.cgsCoreStringBase0xc = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.cgsCoreStringBase0x14 = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.cgsCoreStringBase0x1c = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.cgsCoreStringBase0x24 = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.cgsResourceHandle0x2c = (this._io.readBytes(8)) as any
      this.cgsResourceHandle0x34 = (this._io.readBytes(8)) as any
      this.cgsResourceHandle0x3c = (this._io.readBytes(8)) as any
      this.gameChangerId0x44 = (this._io.readU4be()) as any
      this.unkEnum0x48 = (this._io.readU4be()) as any
      this.ptrGenesysGenUielementBase0x4c = (this._io.readU4be()) as any
      this.int32T0x50 = (this._io.readS4be()) as any
      this.int32T0x54 = (this._io.readS4be()) as any
      this.int32T0x58 = (this._io.readS4be()) as any
      this.int32T0x5c = (this._io.readS4be()) as any
      this.int32T0x60 = (this._io.readS4be()) as any
      this.unkEnum0x64 = (this._io.readU2be()) as any
      this.arrayCountFor0x48 = (this._io.readU2be()) as any
    }

    private _inst00002a7c110x48: Array<number | undefined> | undefined;
    get inst00002a7c110x48(): Array<number | undefined> | undefined {
      if (typeof this._inst00002a7c110x48 !== 'undefined')
        return this._inst00002a7c110x48;
      if ((this.unkEnum0x48 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.unkEnum0x48 as any));
        this._inst00002a7c110x48 = [];
        for (let i = 0; i < (this.arrayCountFor0x48 as any); i++) {
          this._inst00002a7c110x48.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._inst00002a7c110x48;
    }

    private _instGenesysGenUielementBase0x4c: GenericGenObject.GenesysGenUielementBase | undefined;
    get instGenesysGenUielementBase0x4c(): GenericGenObject.GenesysGenUielementBase | undefined {
      if (typeof this._instGenesysGenUielementBase0x4c !== 'undefined')
        return this._instGenesysGenUielementBase0x4c;
      if ((this.ptrGenesysGenUielementBase0x4c as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrGenesysGenUielementBase0x4c as any));
        this._instGenesysGenUielementBase0x4c = (new GenericGenObject.GenesysGenUielementBase(this._io, this, this._root)) as any
        this._io.seek(_pos);
      }
      return this._instGenesysGenUielementBase0x4c;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (104) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (4075515997) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    cgsCoreStringBase0xc: GenericGenObject.StringBase;
    cgsCoreStringBase0x14: GenericGenObject.StringBase;
    cgsCoreStringBase0x1c: GenericGenObject.StringBase;
    cgsCoreStringBase0x24: GenericGenObject.StringBase;
    cgsResourceHandle0x2c: Uint8Array;
    cgsResourceHandle0x34: Uint8Array;
    cgsResourceHandle0x3c: Uint8Array;
    gameChangerId0x44: number;

    /**
     * enum; 00_00_2a_7c_1_1
     */
    unkEnum0x48: number;
    ptrGenesysGenUielementBase0x4c: number;
    int32T0x50: number;
    int32T0x54: number;
    int32T0x58: number;
    int32T0x5c: number;
    int32T0x60: number;

    /**
     * enum; 06_a9_64_cd
     */
    unkEnum0x64: number;
    arrayCountFor0x48: number;
  }
}

export namespace GenericGenObject {
  export class T00045fB1 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenPhysicsSequenceItemPhysicsDoubleValue {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.ptrModulatingValue0x10 = (this._io.readU4be()) as any
      this.automatedProperty0x14 = (this._io.readU4be()) as any
    }

    private _instModulatingValue0x10: number | undefined;
    get instModulatingValue0x10(): number | undefined {
      if (typeof this._instModulatingValue0x10 !== 'undefined')
        return this._instModulatingValue0x10;
      if ((this.ptrModulatingValue0x10 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrModulatingValue0x10 as any));
        this._instModulatingValue0x10 = (this._io.readU4be()) as any
        this._io.seek(_pos);
      }
      return this._instModulatingValue0x10;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (24) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3956246192) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;

    /**
     * enum; 00_03_f6_5a_1
     */
    ptrModulatingValue0x10: number;

    /**
     * enum; 00_03_f7_15_1
     */
    automatedProperty0x14: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenHeatLevel {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.aimForPayloadTime0x10 = (this._io.readF4be()) as any
      this.float32T0x14 = (this._io.readF4be()) as any
      this.float32T0x18 = (this._io.readF4be()) as any
      this.copHearingRangeForIdlePlayer0x1c = (this._io.readF4be()) as any
      this.copHearingRangeForMovingPlayer0x20 = (this._io.readF4be()) as any
      this.copSightConeAngleWhenAlert0x24 = (this._io.readF4be()) as any
      this.copSightConeAngleWhenIdle0x28 = (this._io.readF4be()) as any
      this.copSightRangeWhenAlert0x2c = (this._io.readF4be()) as any
      this.copSightRangeWhenChasing0x30 = (this._io.readF4be()) as any
      this.copSightRangeWhenIdle0x34 = (this._io.readF4be()) as any
      this.float32T0x38 = (this._io.readF4be()) as any
      this.unkEnum0x3c = (this._io.readU4be()) as any
      this.threshold0x40 = (this._io.readU4be()) as any
      this.ptrArrFormationAhead0x44 = (this._io.readU4be()) as any
      this.ptrArrFormationBehind0x48 = (this._io.readU4be()) as any
      this.arrayCountFor0x3c = (this._io.readU2be()) as any
      this.arrayCountFor0x44 = (this._io.readU2be()) as any
      this.arrayCountFor0x48 = (this._io.readU2be()) as any
      this.allowCooldown0x52 = (this._io.readU1()) as any
      this.forceCooldown0x53 = (this._io.readU1()) as any
      this.aimForPayloadAngle0x54 = (this._io.readU1()) as any
      this.displayNumber0x55 = (this._io.readU1()) as any
      this.uint8T0x56 = (this._io.readU1()) as any
      this.uint8T0x57 = (this._io.readU1()) as any
      this.uint8T0x58 = (this._io.readU1()) as any
      this.uint8T0x59 = (this._io.readU1()) as any
      this.uint8T0x5a = (this._io.readU1()) as any
      this.uint8T0x5b = (this._io.readU1()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (92) as any
      return this._size;
    }

    private _inst0006FcF910x3c: Array<number | undefined> | undefined;
    get inst0006FcF910x3c(): Array<number | undefined> | undefined {
      if (typeof this._inst0006FcF910x3c !== 'undefined')
        return this._inst0006FcF910x3c;
      if ((this.unkEnum0x3c as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.unkEnum0x3c as any));
        this._inst0006FcF910x3c = [];
        for (let i = 0; i < (this.arrayCountFor0x3c as any); i++) {
          this._inst0006FcF910x3c.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._inst0006FcF910x3c;
    }

    private _instFormationBehind0x48: Array<number | undefined> | undefined;
    get instFormationBehind0x48(): Array<number | undefined> | undefined {
      if (typeof this._instFormationBehind0x48 !== 'undefined')
        return this._instFormationBehind0x48;
      if ((this.ptrArrFormationBehind0x48 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrFormationBehind0x48 as any));
        this._instFormationBehind0x48 = [];
        for (let i = 0; i < (this.arrayCountFor0x48 as any); i++) {
          this._instFormationBehind0x48.push(this._io.readU1());
        }
        this._io.seek(_pos);
      }
      return this._instFormationBehind0x48;
    }

    private _instFormationAhead0x44: Array<number | undefined> | undefined;
    get instFormationAhead0x44(): Array<number | undefined> | undefined {
      if (typeof this._instFormationAhead0x44 !== 'undefined')
        return this._instFormationAhead0x44;
      if ((this.ptrArrFormationAhead0x44 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrFormationAhead0x44 as any));
        this._instFormationAhead0x44 = [];
        for (let i = 0; i < (this.arrayCountFor0x44 as any); i++) {
          this._instFormationAhead0x44.push(this._io.readU1());
        }
        this._io.seek(_pos);
      }
      return this._instFormationAhead0x44;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2286540362) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    aimForPayloadTime0x10: number;
    float32T0x14: number;
    float32T0x18: number;
    copHearingRangeForIdlePlayer0x1c: number;
    copHearingRangeForMovingPlayer0x20: number;
    copSightConeAngleWhenAlert0x24: number;
    copSightConeAngleWhenIdle0x28: number;
    copSightRangeWhenAlert0x2c: number;
    copSightRangeWhenChasing0x30: number;
    copSightRangeWhenIdle0x34: number;
    float32T0x38: number;

    /**
     * enum; 00_06_fc_f9_1
     */
    unkEnum0x3c: number;
    threshold0x40: number;
    ptrArrFormationAhead0x44: number;
    ptrArrFormationBehind0x48: number;
    arrayCountFor0x3c: number;

    /**
     * "FormationAheadCount"
     */
    arrayCountFor0x44: number;

    /**
     * "FormationBehindCount"
     */
    arrayCountFor0x48: number;
    allowCooldown0x52: number;
    forceCooldown0x53: number;
    aimForPayloadAngle0x54: number;
    displayNumber0x55: number;
    uint8T0x56: number;
    uint8T0x57: number;
    uint8T0x58: number;
    uint8T0x59: number;
    uint8T0x5a: number;
    uint8T0x5b: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenGameplayMilestoneEntry {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.int32T0x10 = (this._io.readS4be()) as any
      this.value0x14 = (this._io.readS4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (24) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1848619037) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    int32T0x10: number;
    value0x14: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenStorePackList {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.ptrArrStorePacks0x10 = (this._io.readU4be()) as any
      this.arrayCountFor0x10 = (this._io.readU2be()) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _instStorePacks0x10: Array<GenericGenObject.CgsResourceHandle | undefined> | undefined;
    get instStorePacks0x10(): Array<GenericGenObject.CgsResourceHandle | undefined> | undefined {
      if (typeof this._instStorePacks0x10 !== 'undefined')
        return this._instStorePacks0x10;
      if ((this.ptrArrStorePacks0x10 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrStorePacks0x10 as any));
        this._instStorePacks0x10 = [];
        for (let i = 0; i < (this.arrayCountFor0x10 as any); i++) {
          this._instStorePacks0x10.push(new GenericGenObject.CgsResourceHandle(this._io, this, this._root));
        }
        this._io.seek(_pos);
      }
      return this._instStorePacks0x10;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (24) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3573113074) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    ptrArrStorePacks0x10: number;

    /**
     * "StorePacksCount"
     */
    arrayCountFor0x10: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenOnlineEvent {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenEvent(this._io, this, this._root)) as any
      this.arena0x30 = (this._io.readU4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (52) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2711283431) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenEvent;
    arena0x30: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenGameUnlock {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.entitlementRequired0xc = (this._io.readBytes(8)) as any
      this.assetToUnlock0x14 = (this._io.readU4be()) as any
      this.associatedAsset0x18 = (this._io.readU4be()) as any
      this.challengeTargetRequired0x1c = (this._io.readU4be()) as any
      this.cgsCoreUniqueId0x20 = (this._io.readU4be()) as any
      this.gameChangerId0x24 = (this._io.readU4be()) as any
      this.ptrArrImage0x28 = (this._io.readU4be()) as any
      this.unkEnum0x2c = (this._io.readU4be()) as any
      this.unkEnum0x30 = (this._io.readU4be()) as any
      this.bountyRequired0x34 = (this._io.readS4be()) as any
      this.progressionType0x38 = (this._io.readU2be()) as any
      this.arrayCountFor0x2c = (this._io.readU2be()) as any
      this.arrayCountFor0x28 = (this._io.readU2be()) as any
      this.arrayCountFor0x30 = (this._io.readU2be()) as any
      this.isEnabled0x40 = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(3)) as any
    }

    private _inst00002821110x2c: Array<number | undefined> | undefined;
    get inst00002821110x2c(): Array<number | undefined> | undefined {
      if (typeof this._inst00002821110x2c !== 'undefined')
        return this._inst00002821110x2c;
      if ((this.unkEnum0x2c as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.unkEnum0x2c as any));
        this._inst00002821110x2c = [];
        for (let i = 0; i < (this.arrayCountFor0x2c as any); i++) {
          this._inst00002821110x2c.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._inst00002821110x2c;
    }

    private _instImage0x28: Array<number | undefined> | undefined;
    get instImage0x28(): Array<number | undefined> | undefined {
      if (typeof this._instImage0x28 !== 'undefined')
        return this._instImage0x28;
      if ((this.ptrArrImage0x28 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrImage0x28 as any));
        this._instImage0x28 = [];
        for (let i = 0; i < (this.arrayCountFor0x28 as any); i++) {
          this._instImage0x28.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._instImage0x28;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (68) as any
      return this._size;
    }

    private _inst00002821120x30: Array<number | undefined> | undefined;
    get inst00002821120x30(): Array<number | undefined> | undefined {
      if (typeof this._inst00002821120x30 !== 'undefined')
        return this._inst00002821120x30;
      if ((this.unkEnum0x30 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.unkEnum0x30 as any));
        this._inst00002821120x30 = [];
        for (let i = 0; i < (this.arrayCountFor0x30 as any); i++) {
          this._inst00002821120x30.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._inst00002821120x30;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2537571270) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    entitlementRequired0xc: Uint8Array;
    assetToUnlock0x14: number;
    associatedAsset0x18: number;
    challengeTargetRequired0x1c: number;
    cgsCoreUniqueId0x20: number;
    gameChangerId0x24: number;
    ptrArrImage0x28: number;

    /**
     * enum; 00_00_28_21_1_1
     */
    unkEnum0x2c: number;

    /**
     * enum; 00_00_28_21_1_2
     */
    unkEnum0x30: number;
    bountyRequired0x34: number;

    /**
     * enum; 0c_96_6a_95
     */
    progressionType0x38: number;
    arrayCountFor0x2c: number;
    arrayCountFor0x28: number;
    arrayCountFor0x30: number;
    isEnabled0x40: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenSlowMoSequenceItem {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenSequenceItem(this._io, this, this._root)) as any
      this.unkEnum0x20 = (this._io.readU4be()) as any
    }

    private _inst0003F65a10x20: number | undefined;
    get inst0003F65a10x20(): number | undefined {
      if (typeof this._inst0003F65a10x20 !== 'undefined')
        return this._inst0003F65a10x20;
      if ((this.unkEnum0x20 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.unkEnum0x20 as any));
        this._inst0003F65a10x20 = (this._io.readU4be()) as any
        this._io.seek(_pos);
      }
      return this._inst0003F65a10x20;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (36) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2470623620) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenSequenceItem;

    /**
     * enum; 00_03_f6_5a_1
     */
    unkEnum0x20: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenPostFxKeyframeVignette {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.rwMathVpuVector20x10 = (new GenericGenObject.RwMathVpuVector2(this._io, this, this._root)) as any
      this.scale0x20 = (new GenericGenObject.RwMathVpuVector2(this._io, this, this._root)) as any
      this.rwMathVpuVector40x30 = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
      this.rwMathVpuVector40x40 = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
      this.gameChangerId0x50 = (this._io.readU4be()) as any
      this.float32T0x54 = (this._io.readF4be()) as any
      this.fisheyePower0x58 = (this._io.readF4be()) as any
      this.fisheyeScale0x5c = (this._io.readF4be()) as any
      this.fisheyeWarp0x60 = (this._io.readF4be()) as any
      this.sharpness0x64 = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (104) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3180273648) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    rwMathVpuVector20x10: GenericGenObject.RwMathVpuVector2;
    scale0x20: GenericGenObject.RwMathVpuVector2;
    rwMathVpuVector40x30: GenericGenObject.RwMathVpuVector4;
    rwMathVpuVector40x40: GenericGenObject.RwMathVpuVector4;
    gameChangerId0x50: number;
    float32T0x54: number;
    fisheyePower0x58: number;
    fisheyeScale0x5c: number;
    fisheyeWarp0x60: number;
    sharpness0x64: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenChevron {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.roadSection0x10 = (this._io.readU4be()) as any
      this.shouldBlockStart0x14 = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(3)) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (24) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (850192155) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    roadSection0x10: number;
    shouldBlockStart0x14: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class C97eAaDa {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenWcpathAnimationBehaviourAnimationPath {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.path0xc = (this._io.readBytes(8)) as any
      this.gameChangerId0x14 = (this._io.readU4be()) as any
      this.float32T0x18 = (this._io.readF4be()) as any
      this.float32T0x1c = (this._io.readF4be()) as any
      this.float32T0x20 = (this._io.readF4be()) as any
      this.float32T0x24 = (this._io.readF4be()) as any
      this.float32T0x28 = (this._io.readF4be()) as any
      this.float32T0x2c = (this._io.readF4be()) as any
      this.float32T0x30 = (this._io.readF4be()) as any
      this.float32T0x34 = (this._io.readF4be()) as any
      this.bool8T0x38 = (this._io.readU1()) as any
      this.bool8T0x39 = (this._io.readU1()) as any
      this.bool8T0x3a = (this._io.readU1()) as any
      this.bool8T0x3b = (this._io.readU1()) as any
      this.bool8T0x3c = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(3)) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (64) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (4150677881) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    path0xc: Uint8Array;
    gameChangerId0x14: number;
    float32T0x18: number;
    float32T0x1c: number;
    float32T0x20: number;
    float32T0x24: number;
    float32T0x28: number;
    float32T0x2c: number;
    float32T0x30: number;
    float32T0x34: number;
    bool8T0x38: number;
    bool8T0x39: number;
    bool8T0x3a: number;
    bool8T0x3b: number;
    bool8T0x3c: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenUielementMiniMap {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.rwMathVpuVector30x10 = (new GenericGenObject.RwMathVpuVector3(this._io, this, this._root)) as any
      this.rwMathVpuVector40x20 = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
      this.rwMathVpuVector40x30 = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
      this.rwMathVpuVector40x40 = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
      this.rwMathVpuVector40x50 = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
      this.rwMathVpuVector40x60 = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
      this.rwMathVpuVector40x70 = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
      this.rwMathVpuVector40x80 = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
      this.rwMathVpuVector40x90 = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
      this.cgsCoreStringBase0xa0 = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.cgsCoreStringBase0xa8 = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.cgsCoreStringBase0xb0 = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.cgsCoreStringBase0xb8 = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.cgsCoreStringBase0xc0 = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.cgsCoreStringBase0xc8 = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.cgsCoreStringBase0xd0 = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.gameChangerId0xd8 = (this._io.readU4be()) as any
      this.float32T0xdc = (this._io.readF4be()) as any
      this.float32T0xe0 = (this._io.readF4be()) as any
      this.float32T0xe4 = (this._io.readF4be()) as any
      this.float32T0xe8 = (this._io.readF4be()) as any
      this.float32T0xec = (this._io.readF4be()) as any
      this.float32T0xf0 = (this._io.readF4be()) as any
      this.float32T0xf4 = (this._io.readF4be()) as any
      this.minimumSpeed0xf8 = (this._io.readF4be()) as any
      this.float32T0xfc = (this._io.readF4be()) as any
      this.float32T0x100 = (this._io.readF4be()) as any
      this.float32T0x104 = (this._io.readF4be()) as any
      this.float32T0x108 = (this._io.readF4be()) as any
      this.ptrGenesysGenUielementBase0x10c = (this._io.readU4be()) as any
      this.ptrGenesysObject0x110 = (this._io.readU4be()) as any
      this.ptrGenesysObject0x114 = (this._io.readU4be()) as any
      this.ptrArrPtrGenesysObject0x118 = (this._io.readU4be()) as any
      this.ptrMask0x11c = (this._io.readU4be()) as any
      this.ptrGenesysObject0x120 = (this._io.readU4be()) as any
      this.arrayCountFor0x118 = (this._io.readU2be()) as any
      this.bool8T0x126 = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(1)) as any
    }

    private _instGenesysObject0x120: GenericGenObject | undefined;

    /**
     * 'instance of Genesys.Object'
     */
    get instGenesysObject0x120(): GenericGenObject | undefined {
      if (typeof this._instGenesysObject0x120 !== 'undefined')
        return this._instGenesysObject0x120;
      if ((this.ptrGenesysObject0x120 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrGenesysObject0x120 as any));
        this._instGenesysObject0x120 = (new GenericGenObject(this._io, this, null)) as any
        this._io.seek(_pos);
      }
      return this._instGenesysObject0x120;
    }

    private _instMask0x11c: GenericGenObject | undefined;

    /**
     * 'instance of Genesys.Object'
     */
    get instMask0x11c(): GenericGenObject | undefined {
      if (typeof this._instMask0x11c !== 'undefined')
        return this._instMask0x11c;
      if ((this.ptrMask0x11c as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrMask0x11c as any));
        this._instMask0x11c = (new GenericGenObject(this._io, this, null)) as any
        this._io.seek(_pos);
      }
      return this._instMask0x11c;
    }

    private _instGenesysObject0x114: GenericGenObject | undefined;

    /**
     * 'instance of Genesys.Object'
     */
    get instGenesysObject0x114(): GenericGenObject | undefined {
      if (typeof this._instGenesysObject0x114 !== 'undefined')
        return this._instGenesysObject0x114;
      if ((this.ptrGenesysObject0x114 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrGenesysObject0x114 as any));
        this._instGenesysObject0x114 = (new GenericGenObject(this._io, this, null)) as any
        this._io.seek(_pos);
      }
      return this._instGenesysObject0x114;
    }

    private _instGenesysObject0x118: Array<GenericGenObject.Ptr | undefined> | undefined;

    /**
     * 'instance of Genesys.Object'
     */
    get instGenesysObject0x118(): Array<GenericGenObject.Ptr | undefined> | undefined {
      if (typeof this._instGenesysObject0x118 !== 'undefined')
        return this._instGenesysObject0x118;
      if ((this.ptrArrPtrGenesysObject0x118 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrPtrGenesysObject0x118 as any));
        this._instGenesysObject0x118 = [];
        for (let i = 0; i < (this.arrayCountFor0x118 as any); i++) {
          this._instGenesysObject0x118.push(new GenericGenObject.Ptr(this._io, this, this._root, "generic_gen_object"));
        }
        this._io.seek(_pos);
      }
      return this._instGenesysObject0x118;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (296) as any
      return this._size;
    }

    private _instGenesysGenUielementBase0x10c: GenericGenObject.GenesysGenUielementBase | undefined;
    get instGenesysGenUielementBase0x10c(): GenericGenObject.GenesysGenUielementBase | undefined {
      if (typeof this._instGenesysGenUielementBase0x10c !== 'undefined')
        return this._instGenesysGenUielementBase0x10c;
      if ((this.ptrGenesysGenUielementBase0x10c as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrGenesysGenUielementBase0x10c as any));
        this._instGenesysGenUielementBase0x10c = (new GenericGenObject.GenesysGenUielementBase(this._io, this, this._root)) as any
        this._io.seek(_pos);
      }
      return this._instGenesysGenUielementBase0x10c;
    }

    private _instGenesysObject0x110: GenericGenObject | undefined;

    /**
     * 'instance of Genesys.Object'
     */
    get instGenesysObject0x110(): GenericGenObject | undefined {
      if (typeof this._instGenesysObject0x110 !== 'undefined')
        return this._instGenesysObject0x110;
      if ((this.ptrGenesysObject0x110 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrGenesysObject0x110 as any));
        this._instGenesysObject0x110 = (new GenericGenObject(this._io, this, null)) as any
        this._io.seek(_pos);
      }
      return this._instGenesysObject0x110;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1705261723) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    rwMathVpuVector30x10: GenericGenObject.RwMathVpuVector3;
    rwMathVpuVector40x20: GenericGenObject.RwMathVpuVector4;
    rwMathVpuVector40x30: GenericGenObject.RwMathVpuVector4;
    rwMathVpuVector40x40: GenericGenObject.RwMathVpuVector4;
    rwMathVpuVector40x50: GenericGenObject.RwMathVpuVector4;
    rwMathVpuVector40x60: GenericGenObject.RwMathVpuVector4;
    rwMathVpuVector40x70: GenericGenObject.RwMathVpuVector4;
    rwMathVpuVector40x80: GenericGenObject.RwMathVpuVector4;
    rwMathVpuVector40x90: GenericGenObject.RwMathVpuVector4;
    cgsCoreStringBase0xa0: GenericGenObject.StringBase;
    cgsCoreStringBase0xa8: GenericGenObject.StringBase;
    cgsCoreStringBase0xb0: GenericGenObject.StringBase;
    cgsCoreStringBase0xb8: GenericGenObject.StringBase;
    cgsCoreStringBase0xc0: GenericGenObject.StringBase;
    cgsCoreStringBase0xc8: GenericGenObject.StringBase;
    cgsCoreStringBase0xd0: GenericGenObject.StringBase;
    gameChangerId0xd8: number;
    float32T0xdc: number;
    float32T0xe0: number;
    float32T0xe4: number;
    float32T0xe8: number;
    float32T0xec: number;
    float32T0xf0: number;
    float32T0xf4: number;
    minimumSpeed0xf8: number;
    float32T0xfc: number;
    float32T0x100: number;
    float32T0x104: number;
    float32T0x108: number;
    ptrGenesysGenUielementBase0x10c: number;
    ptrGenesysObject0x110: number;
    ptrGenesysObject0x114: number;
    ptrArrPtrGenesysObject0x118: number;
    ptrMask0x11c: number;
    ptrGenesysObject0x120: number;
    arrayCountFor0x118: number;
    bool8T0x126: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenUielementScrollableLabel {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.cgsCoreStringBase0xc = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.cgsCoreStringBase0x14 = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.u1u90x1c = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.gameChangerId0x24 = (this._io.readU4be()) as any
      this.cgsCoreUniqueId0x28 = (this._io.readU4be()) as any
      this.float32T0x2c = (this._io.readF4be()) as any
      this.unkEnum0x30 = (this._io.readU4be()) as any
      this.unkEnum0x34 = (this._io.readU4be()) as any
      this.ptrGenesysGenUielementBase0x38 = (this._io.readU4be()) as any
      this.ptrGenesysObject0x3c = (this._io.readU4be()) as any
      this.int32T0x40 = (this._io.readS4be()) as any
      this.unkEnum0x44 = (this._io.readU2be()) as any
      this.id6afs0x46 = (this._io.readU2be()) as any
      this.bool8T0x48 = (this._io.readU1()) as any
      this.bool8T0x49 = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _inst00002a87120x34: number | undefined;
    get inst00002a87120x34(): number | undefined {
      if (typeof this._inst00002a87120x34 !== 'undefined')
        return this._inst00002a87120x34;
      if ((this.unkEnum0x34 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.unkEnum0x34 as any));
        this._inst00002a87120x34 = (this._io.readU4be()) as any
        this._io.seek(_pos);
      }
      return this._inst00002a87120x34;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (76) as any
      return this._size;
    }

    private _instGenesysObject0x3c: GenericGenObject | undefined;

    /**
     * 'instance of Genesys.Object'
     */
    get instGenesysObject0x3c(): GenericGenObject | undefined {
      if (typeof this._instGenesysObject0x3c !== 'undefined')
        return this._instGenesysObject0x3c;
      if ((this.ptrGenesysObject0x3c as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrGenesysObject0x3c as any));
        this._instGenesysObject0x3c = (new GenericGenObject(this._io, this, null)) as any
        this._io.seek(_pos);
      }
      return this._instGenesysObject0x3c;
    }

    private _instGenesysGenUielementBase0x38: GenericGenObject.GenesysGenUielementBase | undefined;
    get instGenesysGenUielementBase0x38(): GenericGenObject.GenesysGenUielementBase | undefined {
      if (typeof this._instGenesysGenUielementBase0x38 !== 'undefined')
        return this._instGenesysGenUielementBase0x38;
      if ((this.ptrGenesysGenUielementBase0x38 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrGenesysGenUielementBase0x38 as any));
        this._instGenesysGenUielementBase0x38 = (new GenericGenObject.GenesysGenUielementBase(this._io, this, this._root)) as any
        this._io.seek(_pos);
      }
      return this._instGenesysGenUielementBase0x38;
    }

    private _inst00002a87110x30: number | undefined;
    get inst00002a87110x30(): number | undefined {
      if (typeof this._inst00002a87110x30 !== 'undefined')
        return this._inst00002a87110x30;
      if ((this.unkEnum0x30 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.unkEnum0x30 as any));
        this._inst00002a87110x30 = (this._io.readU4be()) as any
        this._io.seek(_pos);
      }
      return this._inst00002a87110x30;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1856748625) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    cgsCoreStringBase0xc: GenericGenObject.StringBase;
    cgsCoreStringBase0x14: GenericGenObject.StringBase;
    u1u90x1c: GenericGenObject.StringBase;
    gameChangerId0x24: number;
    cgsCoreUniqueId0x28: number;
    float32T0x2c: number;

    /**
     * enum; 00_00_2a_87_1_1
     */
    unkEnum0x30: number;

    /**
     * enum; 00_00_2a_87_1_2
     */
    unkEnum0x34: number;
    ptrGenesysGenUielementBase0x38: number;
    ptrGenesysObject0x3c: number;
    int32T0x40: number;

    /**
     * enum; 96_c1_53_69
     */
    unkEnum0x44: number;

    /**
     * enum; 40_99_f3_ac
     */
    id6afs0x46: number;
    bool8T0x48: number;
    bool8T0x49: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenApplyVehicleKickSequenceItem {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenSequenceItem(this._io, this, this._root)) as any
      this.strength0x20 = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (36) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3096674344) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenSequenceItem;
    strength0x20: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenNucleusEntitlementTags {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.ptrArrNucleusTag0x10 = (this._io.readU4be()) as any
      this.arrayCountFor0x10 = (this._io.readU2be()) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _instNucleusTag0x10: Array<GenericGenObject.CgsResourceHandle | undefined> | undefined;
    get instNucleusTag0x10(): Array<GenericGenObject.CgsResourceHandle | undefined> | undefined {
      if (typeof this._instNucleusTag0x10 !== 'undefined')
        return this._instNucleusTag0x10;
      if ((this.ptrArrNucleusTag0x10 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrNucleusTag0x10 as any));
        this._instNucleusTag0x10 = [];
        for (let i = 0; i < (this.arrayCountFor0x10 as any); i++) {
          this._instNucleusTag0x10.push(new GenericGenObject.CgsResourceHandle(this._io, this, this._root));
        }
        this._io.seek(_pos);
      }
      return this._instNucleusTag0x10;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (24) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3131401224) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    ptrArrNucleusTag0x10: number;

    /**
     * "NucleusTagCount"
     */
    arrayCountFor0x10: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenUielementMoviePlayer {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.ptrSize0x10 = (this._io.readU4be()) as any
      this.ptrGenesysGenUielementBase0x14 = (this._io.readU4be()) as any
    }

    private _instSize0x10: number | undefined;
    get instSize0x10(): number | undefined {
      if (typeof this._instSize0x10 !== 'undefined')
        return this._instSize0x10;
      if ((this.ptrSize0x10 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrSize0x10 as any));
        this._instSize0x10 = (this._io.readU4be()) as any
        this._io.seek(_pos);
      }
      return this._instSize0x10;
    }

    private _instGenesysGenUielementBase0x14: GenericGenObject.GenesysGenUielementBase | undefined;
    get instGenesysGenUielementBase0x14(): GenericGenObject.GenesysGenUielementBase | undefined {
      if (typeof this._instGenesysGenUielementBase0x14 !== 'undefined')
        return this._instGenesysGenUielementBase0x14;
      if ((this.ptrGenesysGenUielementBase0x14 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrGenesysGenUielementBase0x14 as any));
        this._instGenesysGenUielementBase0x14 = (new GenericGenObject.GenesysGenUielementBase(this._io, this, this._root)) as any
        this._io.seek(_pos);
      }
      return this._instGenesysGenUielementBase0x14;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (24) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3864748285) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;

    /**
     * enum; 00_00_2a_81_1_1
     */
    ptrSize0x10: number;
    ptrGenesysGenUielementBase0x14: number;
  }
}

export namespace GenericGenObject {
  export class D0007001 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenSpikeStripBlowoutUpgrade {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenWeaponUpgrade(this._io, this, this._root)) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (28) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (41223923) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenWeaponUpgrade;
  }
}

export namespace GenericGenObject {
  export class GenesysGenCameraGameplayShakeEffectRotation {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.pitch0xc = (this._io.readU1()) as any
      this.roll0x34 = (this._io.readU1()) as any
      this.yaw0x5c = (this._io.readU1()) as any
      this.gameChangerId0x84 = (this._io.readU4be()) as any
      this.amplitude0x88 = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (140) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1220037810) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;

    /**
     * enum; 00_06_8f_db_1
     */
    pitch0xc: number;

    /**
     * enum; 00_06_8f_db_1
     */
    roll0x34: number;

    /**
     * enum; 00_06_8f_db_1
     */
    yaw0x5c: number;
    gameChangerId0x84: number;
    amplitude0x88: number;
  }
}

export namespace GenericGenObject {
  export class T95950d30 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenUitechnique {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.cgsCoreStringBase0xc = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.gameChangerId0x14 = (this._io.readU4be()) as any
      this.ptrArrCgsResourceHandle0x18 = (this._io.readU4be()) as any
      this.unkEnum0x1c = (this._io.readU2be()) as any
      this.arrayCountFor0x18 = (this._io.readU2be()) as any
    }

    private _instCgsResourceHandle0x18: Array<GenericGenObject.CgsResourceHandle | undefined> | undefined;
    get instCgsResourceHandle0x18(): Array<GenericGenObject.CgsResourceHandle | undefined> | undefined {
      if (typeof this._instCgsResourceHandle0x18 !== 'undefined')
        return this._instCgsResourceHandle0x18;
      if ((this.ptrArrCgsResourceHandle0x18 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrCgsResourceHandle0x18 as any));
        this._instCgsResourceHandle0x18 = [];
        for (let i = 0; i < (this.arrayCountFor0x18 as any); i++) {
          this._instCgsResourceHandle0x18.push(new GenericGenObject.CgsResourceHandle(this._io, this, this._root));
        }
        this._io.seek(_pos);
      }
      return this._instCgsResourceHandle0x18;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (32) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3638622566) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    cgsCoreStringBase0xc: GenericGenObject.StringBase;
    gameChangerId0x14: number;
    ptrArrCgsResourceHandle0x18: number;

    /**
     * enum; 00_00_31_d2_1
     */
    unkEnum0x1c: number;
    arrayCountFor0x18: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenUielementMainMap {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.rwMathVpuVector30x10 = (new GenericGenObject.RwMathVpuVector3(this._io, this, this._root)) as any
      this.rwMathVpuVector40x20 = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
      this.rwMathVpuVector40x30 = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
      this.rwMathVpuVector40x40 = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
      this.rwMathVpuVector40x50 = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
      this.rwMathVpuVector40x60 = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
      this.rwMathVpuVector40x70 = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
      this.rwMathVpuVector40x80 = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
      this.rwMathVpuVector40x90 = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
      this.cgsCoreStringBase0xa0 = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.cgsCoreStringBase0xa8 = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.cgsCoreStringBase0xb0 = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.cgsCoreStringBase0xb8 = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.cgsCoreStringBase0xc0 = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.cgsCoreStringBase0xc8 = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.cgsCoreStringBase0xd0 = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.gameChangerId0xd8 = (this._io.readU4be()) as any
      this.float32T0xdc = (this._io.readF4be()) as any
      this.float32T0xe0 = (this._io.readF4be()) as any
      this.float32T0xe4 = (this._io.readF4be()) as any
      this.float32T0xe8 = (this._io.readF4be()) as any
      this.float32T0xec = (this._io.readF4be()) as any
      this.float32T0xf0 = (this._io.readF4be()) as any
      this.float32T0xf4 = (this._io.readF4be()) as any
      this.minimumSpeed0xf8 = (this._io.readF4be()) as any
      this.float32T0xfc = (this._io.readF4be()) as any
      this.float32T0x100 = (this._io.readF4be()) as any
      this.float32T0x104 = (this._io.readF4be()) as any
      this.float32T0x108 = (this._io.readF4be()) as any
      this.ptrGenesysGenUielementBase0x10c = (this._io.readU4be()) as any
      this.ptrGenesysObject0x110 = (this._io.readU4be()) as any
      this.ptrGenesysObject0x114 = (this._io.readU4be()) as any
      this.ptrArrPtrGenesysObject0x118 = (this._io.readU4be()) as any
      this.ptrMask0x11c = (this._io.readU4be()) as any
      this.ptrGenesysObject0x120 = (this._io.readU4be()) as any
      this.arrayCountFor0x118 = (this._io.readU2be()) as any
      this.bool8T0x126 = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(1)) as any
    }

    private _instGenesysObject0x120: GenericGenObject | undefined;

    /**
     * 'instance of Genesys.Object'
     */
    get instGenesysObject0x120(): GenericGenObject | undefined {
      if (typeof this._instGenesysObject0x120 !== 'undefined')
        return this._instGenesysObject0x120;
      if ((this.ptrGenesysObject0x120 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrGenesysObject0x120 as any));
        this._instGenesysObject0x120 = (new GenericGenObject(this._io, this, null)) as any
        this._io.seek(_pos);
      }
      return this._instGenesysObject0x120;
    }

    private _instMask0x11c: GenericGenObject | undefined;

    /**
     * 'instance of Genesys.Object'
     */
    get instMask0x11c(): GenericGenObject | undefined {
      if (typeof this._instMask0x11c !== 'undefined')
        return this._instMask0x11c;
      if ((this.ptrMask0x11c as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrMask0x11c as any));
        this._instMask0x11c = (new GenericGenObject(this._io, this, null)) as any
        this._io.seek(_pos);
      }
      return this._instMask0x11c;
    }

    private _instGenesysObject0x114: GenericGenObject | undefined;

    /**
     * 'instance of Genesys.Object'
     */
    get instGenesysObject0x114(): GenericGenObject | undefined {
      if (typeof this._instGenesysObject0x114 !== 'undefined')
        return this._instGenesysObject0x114;
      if ((this.ptrGenesysObject0x114 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrGenesysObject0x114 as any));
        this._instGenesysObject0x114 = (new GenericGenObject(this._io, this, null)) as any
        this._io.seek(_pos);
      }
      return this._instGenesysObject0x114;
    }

    private _instGenesysObject0x118: Array<GenericGenObject.Ptr | undefined> | undefined;

    /**
     * 'instance of Genesys.Object'
     */
    get instGenesysObject0x118(): Array<GenericGenObject.Ptr | undefined> | undefined {
      if (typeof this._instGenesysObject0x118 !== 'undefined')
        return this._instGenesysObject0x118;
      if ((this.ptrArrPtrGenesysObject0x118 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrPtrGenesysObject0x118 as any));
        this._instGenesysObject0x118 = [];
        for (let i = 0; i < (this.arrayCountFor0x118 as any); i++) {
          this._instGenesysObject0x118.push(new GenericGenObject.Ptr(this._io, this, this._root, "generic_gen_object"));
        }
        this._io.seek(_pos);
      }
      return this._instGenesysObject0x118;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (296) as any
      return this._size;
    }

    private _instGenesysGenUielementBase0x10c: GenericGenObject.GenesysGenUielementBase | undefined;
    get instGenesysGenUielementBase0x10c(): GenericGenObject.GenesysGenUielementBase | undefined {
      if (typeof this._instGenesysGenUielementBase0x10c !== 'undefined')
        return this._instGenesysGenUielementBase0x10c;
      if ((this.ptrGenesysGenUielementBase0x10c as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrGenesysGenUielementBase0x10c as any));
        this._instGenesysGenUielementBase0x10c = (new GenericGenObject.GenesysGenUielementBase(this._io, this, this._root)) as any
        this._io.seek(_pos);
      }
      return this._instGenesysGenUielementBase0x10c;
    }

    private _instGenesysObject0x110: GenericGenObject | undefined;

    /**
     * 'instance of Genesys.Object'
     */
    get instGenesysObject0x110(): GenericGenObject | undefined {
      if (typeof this._instGenesysObject0x110 !== 'undefined')
        return this._instGenesysObject0x110;
      if ((this.ptrGenesysObject0x110 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrGenesysObject0x110 as any));
        this._instGenesysObject0x110 = (new GenericGenObject(this._io, this, null)) as any
        this._io.seek(_pos);
      }
      return this._instGenesysObject0x110;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2199276125) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    rwMathVpuVector30x10: GenericGenObject.RwMathVpuVector3;
    rwMathVpuVector40x20: GenericGenObject.RwMathVpuVector4;
    rwMathVpuVector40x30: GenericGenObject.RwMathVpuVector4;
    rwMathVpuVector40x40: GenericGenObject.RwMathVpuVector4;
    rwMathVpuVector40x50: GenericGenObject.RwMathVpuVector4;
    rwMathVpuVector40x60: GenericGenObject.RwMathVpuVector4;
    rwMathVpuVector40x70: GenericGenObject.RwMathVpuVector4;
    rwMathVpuVector40x80: GenericGenObject.RwMathVpuVector4;
    rwMathVpuVector40x90: GenericGenObject.RwMathVpuVector4;
    cgsCoreStringBase0xa0: GenericGenObject.StringBase;
    cgsCoreStringBase0xa8: GenericGenObject.StringBase;
    cgsCoreStringBase0xb0: GenericGenObject.StringBase;
    cgsCoreStringBase0xb8: GenericGenObject.StringBase;
    cgsCoreStringBase0xc0: GenericGenObject.StringBase;
    cgsCoreStringBase0xc8: GenericGenObject.StringBase;
    cgsCoreStringBase0xd0: GenericGenObject.StringBase;
    gameChangerId0xd8: number;
    float32T0xdc: number;
    float32T0xe0: number;
    float32T0xe4: number;
    float32T0xe8: number;
    float32T0xec: number;
    float32T0xf0: number;
    float32T0xf4: number;
    minimumSpeed0xf8: number;
    float32T0xfc: number;
    float32T0x100: number;
    float32T0x104: number;
    float32T0x108: number;
    ptrGenesysGenUielementBase0x10c: number;
    ptrGenesysObject0x110: number;
    ptrGenesysObject0x114: number;
    ptrArrPtrGenesysObject0x118: number;
    ptrMask0x11c: number;
    ptrGenesysObject0x120: number;
    arrayCountFor0x118: number;
    bool8T0x126: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenSequenceItem {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.enabledBinding0xc = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.gameChangerId0x14 = (this._io.readU4be()) as any
      this.endTime0x18 = (this._io.readF4be()) as any
      this.startTime0x1c = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (32) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1766412136) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    enabledBinding0xc: GenericGenObject.StringBase;
    gameChangerId0x14: number;
    endTime0x18: number;
    startTime0x1c: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenWcvfxBehaviourLights {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.lightDefinition0xc = (this._io.readBytes(8)) as any
      this.gameChangerId0x14 = (this._io.readU4be()) as any
      this.locatorGroup0x18 = (this._io.readU4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (28) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3417537371) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    lightDefinition0xc: Uint8Array;
    gameChangerId0x14: number;
    locatorGroup0x18: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenScoringAction {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.predicate0xc = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.ptrArrCgsCoreUniqueId0x14 = (this._io.readU4be()) as any
      this.description0x18 = (this._io.readU4be()) as any
      this.gameChangerId0x1c = (this._io.readU4be()) as any
      this.gameplayTrigger0x20 = (this._io.readU4be()) as any
      this.cgsCoreUniqueId0x24 = (this._io.readU4be()) as any
      this.sequence0x28 = (this._io.readU4be()) as any
      this.cgsCoreUniqueId0x2c = (this._io.readU4be()) as any
      this.title0x30 = (this._io.readU4be()) as any
      this.int32T0x34 = (this._io.readS4be()) as any
      this.heat0x38 = (this._io.readS4be()) as any
      this.priority0x3c = (this._io.readS4be()) as any
      this.score0x40 = (this._io.readS4be()) as any
      this.xp0x44 = (this._io.readS4be()) as any
      this.queue0x48 = (this._io.readU2be()) as any
      this.arrayCountFor0x14 = (this._io.readU2be()) as any
      this.feedbackDeferrable0x4c = (this._io.readU1()) as any
      this.online0x4d = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _instCgsCoreUniqueId0x14: Array<number | undefined> | undefined;
    get instCgsCoreUniqueId0x14(): Array<number | undefined> | undefined {
      if (typeof this._instCgsCoreUniqueId0x14 !== 'undefined')
        return this._instCgsCoreUniqueId0x14;
      if ((this.ptrArrCgsCoreUniqueId0x14 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrCgsCoreUniqueId0x14 as any));
        this._instCgsCoreUniqueId0x14 = [];
        for (let i = 0; i < (this.arrayCountFor0x14 as any); i++) {
          this._instCgsCoreUniqueId0x14.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._instCgsCoreUniqueId0x14;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (80) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2252967758) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    predicate0xc: GenericGenObject.StringBase;
    ptrArrCgsCoreUniqueId0x14: number;
    description0x18: number;
    gameChangerId0x1c: number;
    gameplayTrigger0x20: number;
    cgsCoreUniqueId0x24: number;
    sequence0x28: number;
    cgsCoreUniqueId0x2c: number;
    title0x30: number;
    int32T0x34: number;
    heat0x38: number;
    priority0x3c: number;
    score0x40: number;
    xp0x44: number;

    /**
     * enum; 00_09_37_93_1
     */
    queue0x48: number;
    arrayCountFor0x14: number;
    feedbackDeferrable0x4c: number;
    online0x4d: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenCarSelectDataSequences {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.ptrArrSequences0x10 = (this._io.readU4be()) as any
      this.time0x14 = (this._io.readS4be()) as any
      this.arrayCountFor0x10 = (this._io.readU2be()) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _instSequences0x10: Array<number | undefined> | undefined;
    get instSequences0x10(): Array<number | undefined> | undefined {
      if (typeof this._instSequences0x10 !== 'undefined')
        return this._instSequences0x10;
      if ((this.ptrArrSequences0x10 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrSequences0x10 as any));
        this._instSequences0x10 = [];
        for (let i = 0; i < (this.arrayCountFor0x10 as any); i++) {
          this._instSequences0x10.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._instSequences0x10;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (28) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1668851487) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    ptrArrSequences0x10: number;
    time0x14: number;

    /**
     * "SequencesCount"
     */
    arrayCountFor0x10: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenPostFxstateColourCubeSettings {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.colourCube0xc = (this._io.readBytes(8)) as any
      this.gameChangerId0x14 = (this._io.readU4be()) as any
      this.zeroIfNotSet0x18 = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(3)) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (28) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2006186034) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    colourCube0xc: Uint8Array;
    gameChangerId0x14: number;
    zeroIfNotSet0x18: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenNitrousBurningGameRule {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenGameRule(this._io, this, this._root)) as any
      this.float32T0x10 = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (20) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3502480523) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenGameRule;
    float32T0x10: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenCoronaFlare {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.colour0x10 = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
      this.arrInlineFloat32T0x20 = [];
      for (let i = 0; i < 6; i++) {
        this.arrInlineFloat32T0x20.push(this._io.readF4be());
      }
      this.arrInlineFloat32T0x38 = [];
      for (let i = 0; i < 6; i++) {
        this.arrInlineFloat32T0x38.push(this._io.readF4be());
      }
      this.material0x50 = (this._io.readBytes(8)) as any
      this.gameChangerId0x58 = (this._io.readU4be()) as any
      this.brightness0x5c = (this._io.readF4be()) as any
      this.position0x60 = (this._io.readF4be()) as any
      this.float32T0x64 = (this._io.readF4be()) as any
      this.float32T0x68 = (this._io.readF4be()) as any
      this.rotationOffset0x6c = (this._io.readF4be()) as any
      this.arrayCountFor0x20 = (this._io.readU2be()) as any
      this.arrayCountFor0x38 = (this._io.readU2be()) as any
      this.bool8T0x74 = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(3)) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (120) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2913275356) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    colour0x10: GenericGenObject.RwMathVpuVector4;
    arrInlineFloat32T0x20: Array<number>;
    arrInlineFloat32T0x38: Array<number>;
    material0x50: Uint8Array;
    gameChangerId0x58: number;
    brightness0x5c: number;
    position0x60: number;
    float32T0x64: number;
    float32T0x68: number;
    rotationOffset0x6c: number;
    arrayCountFor0x20: number;
    arrayCountFor0x38: number;
    bool8T0x74: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenPostFxKeyframeBloom {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.colour0x10 = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
      this.gameChangerId0x20 = (this._io.readU4be()) as any
      this.darkBloomWeight0x24 = (this._io.readF4be()) as any
      this.darkBloomWhitePoint0x28 = (this._io.readF4be()) as any
      this.largeWeight0x2c = (this._io.readF4be()) as any
      this.float32T0x30 = (this._io.readF4be()) as any
      this.mediumWeight0x34 = (this._io.readF4be()) as any
      this.saturation0x38 = (this._io.readF4be()) as any
      this.smallWeight0x3c = (this._io.readF4be()) as any
      this.threshold0x40 = (this._io.readF4be()) as any
      this.thresholdLarge0x44 = (this._io.readF4be()) as any
      this.thresholdMedium0x48 = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (76) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3592057837) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    colour0x10: GenericGenObject.RwMathVpuVector4;
    gameChangerId0x20: number;
    darkBloomWeight0x24: number;
    darkBloomWhitePoint0x28: number;
    largeWeight0x2c: number;
    float32T0x30: number;
    mediumWeight0x34: number;
    saturation0x38: number;
    smallWeight0x3c: number;
    threshold0x40: number;
    thresholdLarge0x44: number;
    thresholdMedium0x48: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenMineWeapon {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenWeapon(this._io, this, this._root)) as any
      this.cgsResourceHandle0xb0 = (this._io.readBytes(8)) as any
      this.float32T0xb8 = (this._io.readF4be()) as any
      this.float32T0xbc = (this._io.readF4be()) as any
      this.float32T0xc0 = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (196) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1363031339) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenWeapon;
    cgsResourceHandle0xb0: Uint8Array;
    float32T0xb8: number;
    float32T0xbc: number;
    float32T0xc0: number;
  }
}

export namespace GenericGenObject {
  export class T35D62d64 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenAddBehaviourSequenceItem {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenSequenceItem(this._io, this, this._root)) as any
      this.behaviour0x20 = (this._io.readBytes(8)) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (36) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (4281548263) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenSequenceItem;
    behaviour0x20: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenWcplaySoundBehaviourPropSurfaceSound {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.surface0x10 = (this._io.readU4be()) as any
      this.ptrArrRollingWaves0x14 = (this._io.readU4be()) as any
      this.ptrArrScrapingWaves0x18 = (this._io.readU4be()) as any
      this.ptrArrWaves0x1c = (this._io.readU4be()) as any
      this.arrayCountFor0x14 = (this._io.readU2be()) as any
      this.arrayCountFor0x18 = (this._io.readU2be()) as any
      this.arrayCountFor0x1c = (this._io.readU2be()) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _instWaves0x1c: Array<GenericGenObject.CgsResourceHandle | undefined> | undefined;
    get instWaves0x1c(): Array<GenericGenObject.CgsResourceHandle | undefined> | undefined {
      if (typeof this._instWaves0x1c !== 'undefined')
        return this._instWaves0x1c;
      if ((this.ptrArrWaves0x1c as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrWaves0x1c as any));
        this._instWaves0x1c = [];
        for (let i = 0; i < (this.arrayCountFor0x1c as any); i++) {
          this._instWaves0x1c.push(new GenericGenObject.CgsResourceHandle(this._io, this, this._root));
        }
        this._io.seek(_pos);
      }
      return this._instWaves0x1c;
    }

    private _instRollingWaves0x14: Array<GenericGenObject.CgsResourceHandle | undefined> | undefined;
    get instRollingWaves0x14(): Array<GenericGenObject.CgsResourceHandle | undefined> | undefined {
      if (typeof this._instRollingWaves0x14 !== 'undefined')
        return this._instRollingWaves0x14;
      if ((this.ptrArrRollingWaves0x14 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrRollingWaves0x14 as any));
        this._instRollingWaves0x14 = [];
        for (let i = 0; i < (this.arrayCountFor0x14 as any); i++) {
          this._instRollingWaves0x14.push(new GenericGenObject.CgsResourceHandle(this._io, this, this._root));
        }
        this._io.seek(_pos);
      }
      return this._instRollingWaves0x14;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (40) as any
      return this._size;
    }

    private _instScrapingWaves0x18: Array<GenericGenObject.CgsResourceHandle | undefined> | undefined;
    get instScrapingWaves0x18(): Array<GenericGenObject.CgsResourceHandle | undefined> | undefined {
      if (typeof this._instScrapingWaves0x18 !== 'undefined')
        return this._instScrapingWaves0x18;
      if ((this.ptrArrScrapingWaves0x18 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrScrapingWaves0x18 as any));
        this._instScrapingWaves0x18 = [];
        for (let i = 0; i < (this.arrayCountFor0x18 as any); i++) {
          this._instScrapingWaves0x18.push(new GenericGenObject.CgsResourceHandle(this._io, this, this._root));
        }
        this._io.seek(_pos);
      }
      return this._instScrapingWaves0x18;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3115085927) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    surface0x10: number;
    ptrArrRollingWaves0x14: number;
    ptrArrScrapingWaves0x18: number;
    ptrArrWaves0x1c: number;
    arrayCountFor0x14: number;
    arrayCountFor0x18: number;

    /**
     * "WavesCount"
     */
    arrayCountFor0x1c: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenHudStyleSequenceItem {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenSequenceItem(this._io, this, this._root)) as any
      this.unkEnum0x20 = (this._io.readU4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (36) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (137884438) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenSequenceItem;

    /**
     * enum; 00_05_ab_65_1
     */
    unkEnum0x20: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenCameraGameplayShakeEffect {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.translation0xc = (this._io.readU1()) as any
      this.rotation0xa4 = (this._io.readU1()) as any
      this.gameChangerId0x130 = (this._io.readU4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (308) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3580468080) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;

    /**
     * enum; 00_06_8f_da_1
     */
    translation0xc: number;

    /**
     * enum; 00_06_8f_d9_1
     */
    rotation0xa4: number;
    gameChangerId0x130: number;
  }
}

export namespace GenericGenObject {
  export class T00002fC8 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class T00002fF0 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenThermalVisionModeProperties {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.float32T0x10 = (this._io.readF4be()) as any
      this.float32T0x14 = (this._io.readF4be()) as any
      this.float32T0x18 = (this._io.readF4be()) as any
      this.float32T0x1c = (this._io.readF4be()) as any
      this.float32T0x20 = (this._io.readF4be()) as any
      this.float32T0x24 = (this._io.readF4be()) as any
      this.float32T0x28 = (this._io.readF4be()) as any
      this.float32T0x2c = (this._io.readF4be()) as any
      this.float32T0x30 = (this._io.readF4be()) as any
      this.float32T0x34 = (this._io.readF4be()) as any
      this.float32T0x38 = (this._io.readF4be()) as any
      this.float32T0x3c = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (64) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2721335456) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    float32T0x10: number;
    float32T0x14: number;
    float32T0x18: number;
    float32T0x1c: number;
    float32T0x20: number;
    float32T0x24: number;
    float32T0x28: number;
    float32T0x2c: number;
    float32T0x30: number;
    float32T0x34: number;
    float32T0x38: number;
    float32T0x3c: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenHelicopterWeapon {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenWeapon(this._io, this, this._root)) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (172) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3340139760) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenWeapon;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class T00003022 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenUielementBaseEffectConstant {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.values0x10 = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
      this.binding0x20 = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.cgsCoreStringBase0x28 = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.gameChangerId0x30 = (this._io.readU4be()) as any
      this.int32T0x34 = (this._io.readS4be()) as any
      this.offset0x38 = (this._io.readS4be()) as any
      this.int32T0x3c = (this._io.readS4be()) as any
      this.int32T0x40 = (this._io.readS4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (68) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1862050451) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    values0x10: GenericGenObject.RwMathVpuVector4;
    binding0x20: GenericGenObject.StringBase;
    cgsCoreStringBase0x28: GenericGenObject.StringBase;
    gameChangerId0x30: number;
    int32T0x34: number;
    offset0x38: number;
    int32T0x3c: number;
    int32T0x40: number;
  }
}

export namespace GenericGenObject {
  export class StringBase {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      if ((this.bufOfs as any) < 0) {
        this.saveOfs = (this._io.readBytes(0)) as any
      }
      this.ofsArrBuffer0x0 = (this._io.readU4be()) as any
      this.arrayCountFor0x0 = (this._io.readU4be()) as any
    }

    private _bufOfs: number;
    get bufOfs(): number {
      if (typeof this._bufOfs !== 'undefined')
        return this._bufOfs;
      this._bufOfs = ((this._io as any).pos) as any
      return this._bufOfs;
    }

    private _instBuffer0x0: string;
    get instBuffer0x0(): string {
      if (typeof this._instBuffer0x0 !== 'undefined')
        return this._instBuffer0x0;
      let _pos = this._io.pos;
      this._io.seek(((this.bufOfs as any) + (this.ofsArrBuffer0x0 as any)));
      this._instBuffer0x0 = (KaitaiStream.bytesToStr(this._io.readBytes((this.arrayCountFor0x0 as any)), "ascii")) as any
      this._io.seek(_pos);
      return this._instBuffer0x0;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (12) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2516314814) as any
      return this._muVersionHash;
    }

    saveOfs: Uint8Array | undefined;
    ofsArrBuffer0x0: number;

    /**
     * "Capacity"
     */
    arrayCountFor0x0: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenCameraGameplayShakeEffectRotationAxisParams {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.amplitude0x10 = (this._io.readF4be()) as any
      this.damping0x14 = (this._io.readF4be()) as any
      this.maximumAngle0x18 = (this._io.readF4be()) as any
      this.minimumAngle0x1c = (this._io.readF4be()) as any
      this.springCoefficient0x20 = (this._io.readF4be()) as any
      this.invertForceDirection0x24 = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(3)) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (40) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3652314633) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    amplitude0x10: number;
    damping0x14: number;
    maximumAngle0x18: number;
    minimumAngle0x1c: number;
    springCoefficient0x20: number;
    invertForceDirection0x24: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenUpgradePackage {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.description0xc = (this._io.readU4be()) as any
      this.gameChangerId0x10 = (this._io.readU4be()) as any
      this.image0x14 = (this._io.readU4be()) as any
      this.name0x18 = (this._io.readU4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (28) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3632275044) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    description0xc: number;
    gameChangerId0x10: number;
    image0x14: number;
    name0x18: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenAnimationSequenceItem {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenSequenceItem(this._io, this, this._root)) as any
      this.cgsResourceHandle0x20 = (this._io.readBytes(8)) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (36) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2290736886) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenSequenceItem;
    cgsResourceHandle0x20: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenCoronaEnvMapGlow {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.colour0x10 = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
      this.arrInlineFloat32T0x20 = [];
      for (let i = 0; i < 6; i++) {
        this.arrInlineFloat32T0x20.push(this._io.readF4be());
      }
      this.arrInlineFloat32T0x38 = [];
      for (let i = 0; i < 6; i++) {
        this.arrInlineFloat32T0x38.push(this._io.readF4be());
      }
      this.material0x50 = (this._io.readBytes(8)) as any
      this.gameChangerId0x58 = (this._io.readU4be()) as any
      this.depthBias0x5c = (this._io.readF4be()) as any
      this.float32T0x60 = (this._io.readF4be()) as any
      this.float32T0x64 = (this._io.readF4be()) as any
      this.rotationOffset0x68 = (this._io.readF4be()) as any
      this.arrayCountFor0x20 = (this._io.readU2be()) as any
      this.arrayCountFor0x38 = (this._io.readU2be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (112) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2729521159) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    colour0x10: GenericGenObject.RwMathVpuVector4;
    arrInlineFloat32T0x20: Array<number>;
    arrInlineFloat32T0x38: Array<number>;
    material0x50: Uint8Array;
    gameChangerId0x58: number;
    depthBias0x5c: number;
    float32T0x60: number;
    float32T0x64: number;
    rotationOffset0x68: number;
    arrayCountFor0x20: number;
    arrayCountFor0x38: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenBusMixerChannelSequenceItemBusMixerChannelDoubleValue {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.ptrModulatingValue0x10 = (this._io.readU4be()) as any
      this.busMixerChannelProperty0x14 = (this._io.readU4be()) as any
    }

    private _instModulatingValue0x10: number | undefined;
    get instModulatingValue0x10(): number | undefined {
      if (typeof this._instModulatingValue0x10 !== 'undefined')
        return this._instModulatingValue0x10;
      if ((this.ptrModulatingValue0x10 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrModulatingValue0x10 as any));
        this._instModulatingValue0x10 = (this._io.readU4be()) as any
        this._io.seek(_pos);
      }
      return this._instModulatingValue0x10;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (24) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (41209892) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;

    /**
     * enum; 00_03_f6_5a_1
     */
    ptrModulatingValue0x10: number;

    /**
     * enum; 00_03_f6_d5_1
     */
    busMixerChannelProperty0x14: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenDeviceGrantUpgradePackage {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenUpgradePackage(this._io, this, this._root)) as any
      this.cgsCoreUniqueId0x1c = (this._io.readU4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (32) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (4248992647) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenUpgradePackage;
    cgsCoreUniqueId0x1c: number;
  }
}

export namespace GenericGenObject {
  export class T0007Bc8a {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class T5b3321F5 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class T0006Fa8a {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class T0006Fa71 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenPhysicalExplosionGameplayExplosion {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.float32T0x10 = (this._io.readF4be()) as any
      this.float32T0x14 = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (24) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2442478334) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    float32T0x10: number;
    float32T0x14: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenNucleusGrantMappingsList {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.ptrArrItems0x10 = (this._io.readU4be()) as any
      this.arrayCountFor0x10 = (this._io.readU2be()) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _instItems0x10: Array<number | undefined> | undefined;
    get instItems0x10(): Array<number | undefined> | undefined {
      if (typeof this._instItems0x10 !== 'undefined')
        return this._instItems0x10;
      if ((this.ptrArrItems0x10 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrItems0x10 as any));
        this._instItems0x10 = [];
        for (let i = 0; i < (this.arrayCountFor0x10 as any); i++) {
          this._instItems0x10.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._instItems0x10;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (24) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (975568910) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;

    /**
     * enum; 00_00_33_09_1
     */
    ptrArrItems0x10: number;

    /**
     * "ItemsCount"
     */
    arrayCountFor0x10: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenPhysicalExplosionNonRaceCarExplosion {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.float32T0x10 = (this._io.readF4be()) as any
      this.float32T0x14 = (this._io.readF4be()) as any
      this.float32T0x18 = (this._io.readF4be()) as any
      this.float32T0x1c = (this._io.readF4be()) as any
      this.float32T0x20 = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (36) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (930210423) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    float32T0x10: number;
    float32T0x14: number;
    float32T0x18: number;
    float32T0x1c: number;
    float32T0x20: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenRoadblockInstance {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.placement0x10 = (this._io.readU4be()) as any
      this.type0x14 = (this._io.readU4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (24) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2089690370) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    placement0x10: number;
    type0x14: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenWcvfxBehaviour {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenBehaviour(this._io, this, this._root)) as any
      this.impactEffect0x1c = (this._io.readBytes(8)) as any
      this.cgsResourceHandle0x24 = (this._io.readBytes(8)) as any
      this.flashFrequency0x2c = (this._io.readF4be()) as any
      this.float32T0x30 = (this._io.readF4be()) as any
      this.float32T0x34 = (this._io.readF4be()) as any
      this.nonprocedurallySlocum0x38 = (this._io.readF4be()) as any
      this.float32T0x3c = (this._io.readF4be()) as any
      this.ptrArrCoronas0x40 = (this._io.readU4be()) as any
      this.ptrArrLights0x44 = (this._io.readU4be()) as any
      this.unkEnum0x48 = (this._io.readU4be()) as any
      this.int32T0x4c = (this._io.readS4be()) as any
      this.int32T0x50 = (this._io.readS4be()) as any
      this.arrayCountFor0x40 = (this._io.readU2be()) as any
      this.arrayCountFor0x44 = (this._io.readU2be()) as any
      this.arrayCountFor0x48 = (this._io.readU2be()) as any
      this.bool8T0x5a = (this._io.readU1()) as any
      this.bool8T0x5b = (this._io.readU1()) as any
      this.bool8T0x5c = (this._io.readU1()) as any
      this.bool8T0x5d = (this._io.readU1()) as any
      this.bool8T0x5e = (this._io.readU1()) as any
      this.bool8T0x5f = (this._io.readU1()) as any
      this.bool8T0x60 = (this._io.readU1()) as any
      this.bool8T0x61 = (this._io.readU1()) as any
      this.bool8T0x62 = (this._io.readU1()) as any
      this.bool8T0x63 = (this._io.readU1()) as any
      this.bool8T0x64 = (this._io.readU1()) as any
      this.bool8T0x65 = (this._io.readU1()) as any
      this.bool8T0x66 = (this._io.readU1()) as any
      this.bool8T0x67 = (this._io.readU1()) as any
      this.bool8T0x68 = (this._io.readU1()) as any
      this.bool8T0x69 = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _instLights0x44: Array<number | undefined> | undefined;
    get instLights0x44(): Array<number | undefined> | undefined {
      if (typeof this._instLights0x44 !== 'undefined')
        return this._instLights0x44;
      if ((this.ptrArrLights0x44 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrLights0x44 as any));
        this._instLights0x44 = [];
        for (let i = 0; i < (this.arrayCountFor0x44 as any); i++) {
          this._instLights0x44.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._instLights0x44;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (108) as any
      return this._size;
    }

    private _instCoronas0x40: Array<number | undefined> | undefined;
    get instCoronas0x40(): Array<number | undefined> | undefined {
      if (typeof this._instCoronas0x40 !== 'undefined')
        return this._instCoronas0x40;
      if ((this.ptrArrCoronas0x40 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrCoronas0x40 as any));
        this._instCoronas0x40 = [];
        for (let i = 0; i < (this.arrayCountFor0x40 as any); i++) {
          this._instCoronas0x40.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._instCoronas0x40;
    }

    private _inst0000339310x48: Array<number | undefined> | undefined;
    get inst0000339310x48(): Array<number | undefined> | undefined {
      if (typeof this._inst0000339310x48 !== 'undefined')
        return this._inst0000339310x48;
      if ((this.unkEnum0x48 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.unkEnum0x48 as any));
        this._inst0000339310x48 = [];
        for (let i = 0; i < (this.arrayCountFor0x48 as any); i++) {
          this._inst0000339310x48.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._inst0000339310x48;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (32647085) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenBehaviour;
    impactEffect0x1c: Uint8Array;
    cgsResourceHandle0x24: Uint8Array;
    flashFrequency0x2c: number;
    float32T0x30: number;
    float32T0x34: number;
    nonprocedurallySlocum0x38: number;
    float32T0x3c: number;

    /**
     * enum; 00_00_33_92_1
     */
    ptrArrCoronas0x40: number;

    /**
     * enum; 00_00_33_94_1
     */
    ptrArrLights0x44: number;

    /**
     * enum; 00_00_33_93_1
     */
    unkEnum0x48: number;
    int32T0x4c: number;
    int32T0x50: number;

    /**
     * "CoronasCount"
     */
    arrayCountFor0x40: number;

    /**
     * "LightsCount"
     */
    arrayCountFor0x44: number;
    arrayCountFor0x48: number;
    bool8T0x5a: number;
    bool8T0x5b: number;
    bool8T0x5c: number;
    bool8T0x5d: number;
    bool8T0x5e: number;
    bool8T0x5f: number;
    bool8T0x60: number;
    bool8T0x61: number;
    bool8T0x62: number;
    bool8T0x63: number;
    bool8T0x64: number;
    bool8T0x65: number;
    bool8T0x66: number;
    bool8T0x67: number;
    bool8T0x68: number;
    bool8T0x69: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class RwMathVpuVector2 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.arrInlineElements0x0 = [];
      for (let i = 0; i < 2; i++) {
        this.arrInlineElements0x0.push(this._io.readF4be());
      }
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (4) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (786918963) as any
      return this._muVersionHash;
    }

    arrInlineElements0x0: Array<number>;
  }
}

export namespace GenericGenObject {
  export class T0004634a {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class T70F4BbE0 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenAiplayerInstance {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.placement0x10 = (this._io.readU4be()) as any
      this.type0x14 = (this._io.readU4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (24) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2775196711) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    placement0x10: number;
    type0x14: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenPhysicsSequenceItem {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenSequenceItem(this._io, this, this._root)) as any
      this.ptrArrAutomatedValues0x20 = (this._io.readU4be()) as any
      this.arrayCountFor0x20 = (this._io.readU2be()) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _instAutomatedValues0x20: Array<number | undefined> | undefined;
    get instAutomatedValues0x20(): Array<number | undefined> | undefined {
      if (typeof this._instAutomatedValues0x20 !== 'undefined')
        return this._instAutomatedValues0x20;
      if ((this.ptrArrAutomatedValues0x20 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrAutomatedValues0x20 as any));
        this._instAutomatedValues0x20 = [];
        for (let i = 0; i < (this.arrayCountFor0x20 as any); i++) {
          this._instAutomatedValues0x20.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._instAutomatedValues0x20;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (40) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1542147887) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenSequenceItem;

    /**
     * enum; 00_03_f7_14_1
     */
    ptrArrAutomatedValues0x20: number;

    /**
     * "Automated_ValuesCount"
     */
    arrayCountFor0x20: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenPhysicalDefinition {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.localAabbcenter0x10 = (new GenericGenObject.RwMathVpuVector3(this._io, this, this._root)) as any
      this.localAabbhalfDiagonal0x20 = (new GenericGenObject.RwMathVpuVector3(this._io, this, this._root)) as any
      this.additionalInfo0x30 = (this._io.readBytes(8)) as any
      this.ptrArrRigidBodiesNames0x38 = (this._io.readU4be()) as any
      this.gameChangerId0x3c = (this._io.readU4be()) as any
      this.ptrArrRigidBodies0x40 = (this._io.readU4be()) as any
      this.gameChangerId0x44 = (this._io.readS4be()) as any
      this.mainRigidBodyIndex0x48 = (this._io.readS4be()) as any
      this.arrayCountFor0x40 = (this._io.readU2be()) as any
      this.arrayCountFor0x38 = (this._io.readU2be()) as any
    }

    private _instRigidBodiesNames0x38: Array<GenericGenObject.StringBase | undefined> | undefined;
    get instRigidBodiesNames0x38(): Array<GenericGenObject.StringBase | undefined> | undefined {
      if (typeof this._instRigidBodiesNames0x38 !== 'undefined')
        return this._instRigidBodiesNames0x38;
      if ((this.ptrArrRigidBodiesNames0x38 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrRigidBodiesNames0x38 as any));
        this._instRigidBodiesNames0x38 = [];
        for (let i = 0; i < (this.arrayCountFor0x38 as any); i++) {
          this._instRigidBodiesNames0x38.push(new GenericGenObject.StringBase(this._io, this, this._root));
        }
        this._io.seek(_pos);
      }
      return this._instRigidBodiesNames0x38;
    }

    private _instRigidBodies0x40: Array<GenericGenObject.GenesysGenPhysicalDefinitionRigidBody | undefined> | undefined;
    get instRigidBodies0x40(): Array<GenericGenObject.GenesysGenPhysicalDefinitionRigidBody | undefined> | undefined {
      if (typeof this._instRigidBodies0x40 !== 'undefined')
        return this._instRigidBodies0x40;
      if ((this.ptrArrRigidBodies0x40 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrRigidBodies0x40 as any));
        this._instRigidBodies0x40 = [];
        for (let i = 0; i < (this.arrayCountFor0x40 as any); i++) {
          this._instRigidBodies0x40.push(new GenericGenObject.GenesysGenPhysicalDefinitionRigidBody(this._io, this, this._root));
        }
        this._io.seek(_pos);
      }
      return this._instRigidBodies0x40;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (80) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2462007859) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    localAabbcenter0x10: GenericGenObject.RwMathVpuVector3;
    localAabbhalfDiagonal0x20: GenericGenObject.RwMathVpuVector3;
    additionalInfo0x30: Uint8Array;
    ptrArrRigidBodiesNames0x38: number;
    gameChangerId0x3c: number;
    ptrArrRigidBodies0x40: number;
    gameChangerId0x44: number;
    mainRigidBodyIndex0x48: number;

    /**
     * "RigidBodiesCount"
     */
    arrayCountFor0x40: number;

    /**
     * "RigidBodiesNamesCount"
     */
    arrayCountFor0x38: number;
  }
}

export namespace GenericGenObject {
  export class T00045fAd {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenEnvironmentKeyframeLightRig {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.rwMathVpuVector40x10 = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
      this.rwMathVpuVector40x20 = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
      this.rwMathVpuVector40x30 = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
      this.rwMathVpuVector40x40 = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
      this.rwMathVpuVector40x50 = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
      this.rwMathVpuVector40x60 = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
      this.rwMathVpuVector40x70 = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
      this.gameChangerId0x80 = (this._io.readU4be()) as any
      this.float32T0x84 = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (136) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1683395683) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    rwMathVpuVector40x10: GenericGenObject.RwMathVpuVector4;
    rwMathVpuVector40x20: GenericGenObject.RwMathVpuVector4;
    rwMathVpuVector40x30: GenericGenObject.RwMathVpuVector4;
    rwMathVpuVector40x40: GenericGenObject.RwMathVpuVector4;
    rwMathVpuVector40x50: GenericGenObject.RwMathVpuVector4;
    rwMathVpuVector40x60: GenericGenObject.RwMathVpuVector4;
    rwMathVpuVector40x70: GenericGenObject.RwMathVpuVector4;
    gameChangerId0x80: number;
    float32T0x84: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenPhysicalExplosionRaceCarInAirExplosion {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.float32T0x10 = (this._io.readF4be()) as any
      this.float32T0x14 = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (24) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2027177213) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    float32T0x10: number;
    float32T0x14: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenWeaponList {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.ptrArrCgsResourceHandle0x10 = (this._io.readU4be()) as any
      this.arrayCountFor0x10 = (this._io.readU2be()) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _instCgsResourceHandle0x10: Array<GenericGenObject.CgsResourceHandle | undefined> | undefined;
    get instCgsResourceHandle0x10(): Array<GenericGenObject.CgsResourceHandle | undefined> | undefined {
      if (typeof this._instCgsResourceHandle0x10 !== 'undefined')
        return this._instCgsResourceHandle0x10;
      if ((this.ptrArrCgsResourceHandle0x10 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrCgsResourceHandle0x10 as any));
        this._instCgsResourceHandle0x10 = [];
        for (let i = 0; i < (this.arrayCountFor0x10 as any); i++) {
          this._instCgsResourceHandle0x10.push(new GenericGenObject.CgsResourceHandle(this._io, this, this._root));
        }
        this._io.seek(_pos);
      }
      return this._instCgsResourceHandle0x10;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (24) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1701879475) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    ptrArrCgsResourceHandle0x10: number;
    arrayCountFor0x10: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenSequenceTimelineController {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.enabledBinding0xc = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.gameChangerId0x14 = (this._io.readU4be()) as any
      this.triggerType0x18 = (this._io.readU2be()) as any
      this.testContinuously0x1a = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(1)) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (28) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (4067794056) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    enabledBinding0xc: GenericGenObject.StringBase;
    gameChangerId0x14: number;

    /**
     * enum; 00_04_63_4a_1
     */
    triggerType0x18: number;
    testContinuously0x1a: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenUielementPrototypeLabelTextProperties {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.rwMathVpuVector40x10 = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
      this.cgsCoreStringBase0x20 = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.cgsResourceHandle0x28 = (this._io.readBytes(8)) as any
      this.gameChangerId0x30 = (this._io.readU4be()) as any
      this.unoO0x34 = (this._io.readU2be()) as any
      this.bool8T0x36 = (this._io.readU1()) as any
      this.bool8T0x37 = (this._io.readU1()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (56) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3285476138) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    rwMathVpuVector40x10: GenericGenObject.RwMathVpuVector4;
    cgsCoreStringBase0x20: GenericGenObject.StringBase;
    cgsResourceHandle0x28: Uint8Array;
    gameChangerId0x30: number;

    /**
     * enum; 70_f4_bb_e0
     */
    unoO0x34: number;
    bool8T0x36: number;
    bool8T0x37: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenThankyouMapping {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.nucleusEntitlement0xc = (this._io.readBytes(8)) as any
      this.thankyouItem0x14 = (this._io.readBytes(8)) as any
      this.gameChangerId0x1c = (this._io.readU4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (32) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1671215869) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    nucleusEntitlement0xc: Uint8Array;
    thankyouItem0x14: Uint8Array;
    gameChangerId0x1c: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenEventArenaData {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.loadingPointLocation0x10 = (this._io.readU4be()) as any
      this.ptrArrSpawnLocations0x14 = (this._io.readU4be()) as any
      this.ptrArrPtrChevrons0x18 = (this._io.readU4be()) as any
      this.ptrArrPtrCustomChevronList0x1c = (this._io.readU4be()) as any
      this.arrayCountFor0x18 = (this._io.readU2be()) as any
      this.arrayCountFor0x14 = (this._io.readU2be()) as any
      this.arrayCountFor0x1c = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(3)) as any
    }

    private _instSpawnLocations0x14: Array<number | undefined> | undefined;
    get instSpawnLocations0x14(): Array<number | undefined> | undefined {
      if (typeof this._instSpawnLocations0x14 !== 'undefined')
        return this._instSpawnLocations0x14;
      if ((this.ptrArrSpawnLocations0x14 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrSpawnLocations0x14 as any));
        this._instSpawnLocations0x14 = [];
        for (let i = 0; i < (this.arrayCountFor0x14 as any); i++) {
          this._instSpawnLocations0x14.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._instSpawnLocations0x14;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (40) as any
      return this._size;
    }

    private _instCustomChevronList0x1c: Array<GenericGenObject.Ptr | undefined> | undefined;
    get instCustomChevronList0x1c(): Array<GenericGenObject.Ptr | undefined> | undefined {
      if (typeof this._instCustomChevronList0x1c !== 'undefined')
        return this._instCustomChevronList0x1c;
      if ((this.ptrArrPtrCustomChevronList0x1c as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrPtrCustomChevronList0x1c as any));
        this._instCustomChevronList0x1c = [];
        for (let i = 0; i < (this.arrayCountFor0x1c as any); i++) {
          this._instCustomChevronList0x1c.push(new GenericGenObject.Ptr(this._io, this, this._root, "u4"));
        }
        this._io.seek(_pos);
      }
      return this._instCustomChevronList0x1c;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2935374172) as any
      return this._muVersionHash;
    }

    private _instChevrons0x18: Array<GenericGenObject.Ptr | undefined> | undefined;
    get instChevrons0x18(): Array<GenericGenObject.Ptr | undefined> | undefined {
      if (typeof this._instChevrons0x18 !== 'undefined')
        return this._instChevrons0x18;
      if ((this.ptrArrPtrChevrons0x18 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrPtrChevrons0x18 as any));
        this._instChevrons0x18 = [];
        for (let i = 0; i < (this.arrayCountFor0x18 as any); i++) {
          this._instChevrons0x18.push(new GenericGenObject.Ptr(this._io, this, this._root, "u4"));
        }
        this._io.seek(_pos);
      }
      return this._instChevrons0x18;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    loadingPointLocation0x10: number;
    ptrArrSpawnLocations0x14: number;

    /**
     * enum; 00_04_62_44_1
     */
    ptrArrPtrChevrons0x18: number;

    /**
     * enum; 00_06_fa_9f_1
     */
    ptrArrPtrCustomChevronList0x1c: number;

    /**
     * "ChevronsCount"
     */
    arrayCountFor0x18: number;

    /**
     * "Spawn_LocationsCount"
     */
    arrayCountFor0x14: number;

    /**
     * "CustomChevronListCount"
     */
    arrayCountFor0x1c: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenFastLaunchWeaponUpgrade {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenWeaponUpgrade(this._io, this, this._root)) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (28) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3966750237) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenWeaponUpgrade;
  }
}

export namespace GenericGenObject {
  export class GenesysGenWchideBehaviour {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenBehaviour(this._io, this, this._root)) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (32) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1566205417) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenBehaviour;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenWaveSequenceItem {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenSequenceItem(this._io, this, this._root)) as any
      this.fadeIn0x20 = (this._io.readU1()) as any
      this.fadeOut0x38 = (this._io.readU1()) as any
      this.snapshotProperty0x50 = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.transformOverrideBinding0x58 = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.mixerChannel0x60 = (this._io.readBytes(8)) as any
      this.ptrArrWaves0x68 = (this._io.readU4be()) as any
      this.ptrGain0x6c = (this._io.readU4be()) as any
      this.ptrPitch0x70 = (this._io.readU4be()) as any
      this.type0x74 = (this._io.readU2be()) as any
      this.arrayCountFor0x68 = (this._io.readU2be()) as any
      this.autoPitch0x78 = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(3)) as any
    }

    private _instPitch0x70: number | undefined;
    get instPitch0x70(): number | undefined {
      if (typeof this._instPitch0x70 !== 'undefined')
        return this._instPitch0x70;
      if ((this.ptrPitch0x70 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrPitch0x70 as any));
        this._instPitch0x70 = (this._io.readU4be()) as any
        this._io.seek(_pos);
      }
      return this._instPitch0x70;
    }

    private _instGain0x6c: number | undefined;
    get instGain0x6c(): number | undefined {
      if (typeof this._instGain0x6c !== 'undefined')
        return this._instGain0x6c;
      if ((this.ptrGain0x6c as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrGain0x6c as any));
        this._instGain0x6c = (this._io.readU4be()) as any
        this._io.seek(_pos);
      }
      return this._instGain0x6c;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (124) as any
      return this._size;
    }

    private _instWaves0x68: Array<GenericGenObject.CgsResourceHandle | undefined> | undefined;
    get instWaves0x68(): Array<GenericGenObject.CgsResourceHandle | undefined> | undefined {
      if (typeof this._instWaves0x68 !== 'undefined')
        return this._instWaves0x68;
      if ((this.ptrArrWaves0x68 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrWaves0x68 as any));
        this._instWaves0x68 = [];
        for (let i = 0; i < (this.arrayCountFor0x68 as any); i++) {
          this._instWaves0x68.push(new GenericGenObject.CgsResourceHandle(this._io, this, this._root));
        }
        this._io.seek(_pos);
      }
      return this._instWaves0x68;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (897852783) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenSequenceItem;

    /**
     * enum; 00_03_f6_87_1
     */
    fadeIn0x20: number;

    /**
     * enum; 00_03_f6_87_1
     */
    fadeOut0x38: number;
    snapshotProperty0x50: GenericGenObject.StringBase;
    transformOverrideBinding0x58: GenericGenObject.StringBase;
    mixerChannel0x60: Uint8Array;
    ptrArrWaves0x68: number;

    /**
     * enum; 00_03_f6_5a_1
     */
    ptrGain0x6c: number;

    /**
     * enum; 00_03_f6_5a_1
     */
    ptrPitch0x70: number;

    /**
     * enum; 00_03_f3_c4_1
     */
    type0x74: number;

    /**
     * "WavesCount"
     */
    arrayCountFor0x68: number;
    autoPitch0x78: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenVfxSpotEffectSequenceItem {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenSequenceItem(this._io, this, this._root)) as any
      this.rwMathVpuVector30x20 = (new GenericGenObject.RwMathVpuVector3(this._io, this, this._root)) as any
      this.cgsCoreStringBase0x30 = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.cgsResourceHandle0x38 = (this._io.readBytes(8)) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (60) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3678829457) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenSequenceItem;
    rwMathVpuVector30x20: GenericGenObject.RwMathVpuVector3;
    cgsCoreStringBase0x30: GenericGenObject.StringBase;
    cgsResourceHandle0x38: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenUielementBaseTimelineBehaviour {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.cgsCoreStringBase0xc = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.gameChangerId0x14 = (this._io.readU4be()) as any
      this.cgsCoreUniqueId0x18 = (this._io.readU4be()) as any
      this.float32T0x1c = (this._io.readF4be()) as any
      this.duration0x20 = (this._io.readF4be()) as any
      this.type0x24 = (this._io.readU2be()) as any
      this.ease0x26 = (this._io.readU2be()) as any
      this.unkEnum0x28 = (this._io.readU4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (44) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (641453515) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    cgsCoreStringBase0xc: GenericGenObject.StringBase;
    gameChangerId0x14: number;
    cgsCoreUniqueId0x18: number;
    float32T0x1c: number;
    duration0x20: number;

    /**
     * enum; 05_89_a9_77
     */
    type0x24: number;

    /**
     * enum; d0_00_70_01
     */
    ease0x26: number;

    /**
     * enum; 8e_7d_5f_21
     */
    unkEnum0x28: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenEnvironmentKeyframeMiniDof {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.float32T0x10 = (this._io.readF4be()) as any
      this.float32T0x14 = (this._io.readF4be()) as any
      this.float32T0x18 = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (28) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3750941088) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    float32T0x10: number;
    float32T0x14: number;
    float32T0x18: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenWeapon {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.rwMathVpuVector30x10 = (new GenericGenObject.RwMathVpuVector3(this._io, this, this._root)) as any
      this.rwMathVpuVector30x20 = (new GenericGenObject.RwMathVpuVector3(this._io, this, this._root)) as any
      this.cgsResourceHandle0x30 = (this._io.readBytes(8)) as any
      this.cgsResourceHandle0x38 = (this._io.readBytes(8)) as any
      this.cgsResourceHandle0x40 = (this._io.readBytes(8)) as any
      this.cgsResourceHandle0x48 = (this._io.readBytes(8)) as any
      this.cgsResourceHandle0x50 = (this._io.readBytes(8)) as any
      this.cgsResourceHandle0x58 = (this._io.readBytes(8)) as any
      this.gameChangerId0x60 = (this._io.readU4be()) as any
      this.image0x64 = (this._io.readU4be()) as any
      this.name0x68 = (this._io.readU4be()) as any
      this.cgsCoreUniqueId0x6c = (this._io.readU4be()) as any
      this.cgsCoreUniqueId0x70 = (this._io.readU4be()) as any
      this.cgsCoreUniqueId0x74 = (this._io.readU4be()) as any
      this.cgsCoreUniqueId0x78 = (this._io.readU4be()) as any
      this.cgsCoreUniqueId0x7c = (this._io.readU4be()) as any
      this.shortName0x80 = (this._io.readU4be()) as any
      this.ptrArrCgsResourceHandle0x84 = (this._io.readU4be()) as any
      this.float32T0x88 = (this._io.readF4be()) as any
      this.rechargeTime0x8c = (this._io.readF4be()) as any
      this.float32T0x90 = (this._io.readF4be()) as any
      this.unkEnum0x94 = (this._io.readU4be()) as any
      this.unkEnum0x98 = (this._io.readU4be()) as any
      this.unkEnum0x9c = (this._io.readU4be()) as any
      this.unkEnum0xa0 = (this._io.readU2be()) as any
      this.slot0xa2 = (this._io.readU2be()) as any
      this.bool8T0xa4 = (this._io.readU1()) as any
      this.uint8T0xa5 = (this._io.readU1()) as any
      this.arrayCountFor0x84 = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(1)) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (168) as any
      return this._size;
    }

    private _inst00072aBe10x94: number | undefined;
    get inst00072aBe10x94(): number | undefined {
      if (typeof this._inst00072aBe10x94 !== 'undefined')
        return this._inst00072aBe10x94;
      if ((this.unkEnum0x94 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.unkEnum0x94 as any));
        this._inst00072aBe10x94 = (this._io.readU4be()) as any
        this._io.seek(_pos);
      }
      return this._inst00072aBe10x94;
    }

    private _instCgsResourceHandle0x84: Array<GenericGenObject.CgsResourceHandle | undefined> | undefined;
    get instCgsResourceHandle0x84(): Array<GenericGenObject.CgsResourceHandle | undefined> | undefined {
      if (typeof this._instCgsResourceHandle0x84 !== 'undefined')
        return this._instCgsResourceHandle0x84;
      if ((this.ptrArrCgsResourceHandle0x84 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrCgsResourceHandle0x84 as any));
        this._instCgsResourceHandle0x84 = [];
        for (let i = 0; i < (this.arrayCountFor0x84 as any); i++) {
          this._instCgsResourceHandle0x84.push(new GenericGenObject.CgsResourceHandle(this._io, this, this._root));
        }
        this._io.seek(_pos);
      }
      return this._instCgsResourceHandle0x84;
    }

    private _inst00072aBe10x9c: number | undefined;
    get inst00072aBe10x9c(): number | undefined {
      if (typeof this._inst00072aBe10x9c !== 'undefined')
        return this._inst00072aBe10x9c;
      if ((this.unkEnum0x9c as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.unkEnum0x9c as any));
        this._inst00072aBe10x9c = (this._io.readU4be()) as any
        this._io.seek(_pos);
      }
      return this._inst00072aBe10x9c;
    }

    private _inst00072aBe10x98: number | undefined;
    get inst00072aBe10x98(): number | undefined {
      if (typeof this._inst00072aBe10x98 !== 'undefined')
        return this._inst00072aBe10x98;
      if ((this.unkEnum0x98 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.unkEnum0x98 as any));
        this._inst00072aBe10x98 = (this._io.readU4be()) as any
        this._io.seek(_pos);
      }
      return this._inst00072aBe10x98;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3688241096) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    rwMathVpuVector30x10: GenericGenObject.RwMathVpuVector3;
    rwMathVpuVector30x20: GenericGenObject.RwMathVpuVector3;
    cgsResourceHandle0x30: Uint8Array;
    cgsResourceHandle0x38: Uint8Array;
    cgsResourceHandle0x40: Uint8Array;
    cgsResourceHandle0x48: Uint8Array;
    cgsResourceHandle0x50: Uint8Array;
    cgsResourceHandle0x58: Uint8Array;
    gameChangerId0x60: number;
    image0x64: number;
    name0x68: number;
    cgsCoreUniqueId0x6c: number;
    cgsCoreUniqueId0x70: number;
    cgsCoreUniqueId0x74: number;
    cgsCoreUniqueId0x78: number;
    cgsCoreUniqueId0x7c: number;
    shortName0x80: number;
    ptrArrCgsResourceHandle0x84: number;
    float32T0x88: number;
    rechargeTime0x8c: number;
    float32T0x90: number;

    /**
     * enum; 00_07_2a_be_1
     */
    unkEnum0x94: number;

    /**
     * enum; 00_07_2a_be_1
     */
    unkEnum0x98: number;

    /**
     * enum; 00_07_2a_be_1
     */
    unkEnum0x9c: number;

    /**
     * enum; 00_04_5f_ad_1
     */
    unkEnum0xa0: number;

    /**
     * enum; 00_04_5e_f1_1
     */
    slot0xa2: number;
    bool8T0xa4: number;
    uint8T0xa5: number;
    arrayCountFor0x84: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenSetVisionModeTypeSequenceItem {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenSequenceItem(this._io, this, this._root)) as any
      this.cgsResourceHandle0x20 = (this._io.readBytes(8)) as any
      this.unkEnum0x28 = (this._io.readU4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (44) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1583304527) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenSequenceItem;
    cgsResourceHandle0x20: Uint8Array;

    /**
     * enum; 00_07_bc_8a_1
     */
    unkEnum0x28: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenPhysicalDefinitionRigidBodySphereVolume {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.volumeToBodyTransform0x10 = (new GenericGenObject.RwMathVpuMatrix44affine(this._io, this, this._root)) as any
      this.gameChangerId0x50 = (this._io.readU4be()) as any
      this.radius0x54 = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (88) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (4179189423) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    volumeToBodyTransform0x10: GenericGenObject.RwMathVpuMatrix44affine;
    gameChangerId0x50: number;
    radius0x54: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenStorePack {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.packItem0xc = (this._io.readBytes(8)) as any
      this.gameChangerId0x14 = (this._io.readU4be()) as any
      this.ptrArrContentItems0x18 = (this._io.readU4be()) as any
      this.arrayCountFor0x18 = (this._io.readU2be()) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _instContentItems0x18: Array<GenericGenObject.CgsResourceHandle | undefined> | undefined;
    get instContentItems0x18(): Array<GenericGenObject.CgsResourceHandle | undefined> | undefined {
      if (typeof this._instContentItems0x18 !== 'undefined')
        return this._instContentItems0x18;
      if ((this.ptrArrContentItems0x18 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrContentItems0x18 as any));
        this._instContentItems0x18 = [];
        for (let i = 0; i < (this.arrayCountFor0x18 as any); i++) {
          this._instContentItems0x18.push(new GenericGenObject.CgsResourceHandle(this._io, this, this._root));
        }
        this._io.seek(_pos);
      }
      return this._instContentItems0x18;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (32) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3071320584) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    packItem0xc: Uint8Array;
    gameChangerId0x14: number;
    ptrArrContentItems0x18: number;

    /**
     * "ContentItemsCount"
     */
    arrayCountFor0x18: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenUicamera {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.lookAt0x10 = (new GenericGenObject.RwMathVpuVector3(this._io, this, this._root)) as any
      this.position0x20 = (new GenericGenObject.RwMathVpuVector3(this._io, this, this._root)) as any
      this.upVector0x30 = (new GenericGenObject.RwMathVpuVector3(this._io, this, this._root)) as any
      this.gameChangerId0x40 = (this._io.readU4be()) as any
      this.aspectRatio0x44 = (this._io.readF4be()) as any
      this.farClip0x48 = (this._io.readF4be()) as any
      this.fieldOfView0x4c = (this._io.readF4be()) as any
      this.nearClip0x50 = (this._io.readF4be()) as any
      this.aspectCorrect0x54 = (this._io.readU1()) as any
      this.bool8T0x55 = (this._io.readU1()) as any
      this.bool8T0x56 = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(1)) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (88) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (4265727012) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    lookAt0x10: GenericGenObject.RwMathVpuVector3;
    position0x20: GenericGenObject.RwMathVpuVector3;
    upVector0x30: GenericGenObject.RwMathVpuVector3;
    gameChangerId0x40: number;
    aspectRatio0x44: number;
    farClip0x48: number;
    fieldOfView0x4c: number;
    nearClip0x50: number;
    aspectCorrect0x54: number;
    bool8T0x55: number;
    bool8T0x56: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenRoadBlockLayer {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.middleItem0xc = (this._io.readU1()) as any
      this.gameChangerId0x24 = (this._io.readU4be()) as any
      this.distance0x28 = (this._io.readF4be()) as any
      this.firstDistance0x2c = (this._io.readF4be()) as any
      this.ptrArrLeftItems0x30 = (this._io.readU4be()) as any
      this.ptrArrRightItems0x34 = (this._io.readU4be()) as any
      this.arrayCountFor0x30 = (this._io.readU2be()) as any
      this.arrayCountFor0x34 = (this._io.readU2be()) as any
    }

    private _instLeftItems0x30: Array<number | undefined> | undefined;
    get instLeftItems0x30(): Array<number | undefined> | undefined {
      if (typeof this._instLeftItems0x30 !== 'undefined')
        return this._instLeftItems0x30;
      if ((this.ptrArrLeftItems0x30 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrLeftItems0x30 as any));
        this._instLeftItems0x30 = [];
        for (let i = 0; i < (this.arrayCountFor0x30 as any); i++) {
          this._instLeftItems0x30.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._instLeftItems0x30;
    }

    private _instRightItems0x34: Array<number | undefined> | undefined;
    get instRightItems0x34(): Array<number | undefined> | undefined {
      if (typeof this._instRightItems0x34 !== 'undefined')
        return this._instRightItems0x34;
      if ((this.ptrArrRightItems0x34 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrRightItems0x34 as any));
        this._instRightItems0x34 = [];
        for (let i = 0; i < (this.arrayCountFor0x34 as any); i++) {
          this._instRightItems0x34.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._instRightItems0x34;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (60) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1694754426) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;

    /**
     * enum; 00_00_33_2a_1
     */
    middleItem0xc: number;
    gameChangerId0x24: number;
    distance0x28: number;
    firstDistance0x2c: number;

    /**
     * enum; 00_00_33_2a_1
     */
    ptrArrLeftItems0x30: number;

    /**
     * enum; 00_00_33_2a_1
     */
    ptrArrRightItems0x34: number;
    arrayCountFor0x30: number;
    arrayCountFor0x34: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenWcpathAnimationBehaviour {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenBehaviour(this._io, this, this._root)) as any
      this.unkEnum0x1c = (this._io.readU4be()) as any
      this.arrayCountFor0x1c = (this._io.readU2be()) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _inst0000339110x1c: Array<number | undefined> | undefined;
    get inst0000339110x1c(): Array<number | undefined> | undefined {
      if (typeof this._inst0000339110x1c !== 'undefined')
        return this._inst0000339110x1c;
      if ((this.unkEnum0x1c as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.unkEnum0x1c as any));
        this._inst0000339110x1c = [];
        for (let i = 0; i < (this.arrayCountFor0x1c as any); i++) {
          this._inst0000339110x1c.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._inst0000339110x1c;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (36) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (536982309) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenBehaviour;

    /**
     * enum; 00_00_33_91_1
     */
    unkEnum0x1c: number;
    arrayCountFor0x1c: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenPostFxKeyframeGeneral {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.carMotionBlur0x10 = (this._io.readF4be()) as any
      this.worldColourCubeWeight0x14 = (this._io.readF4be()) as any
      this.worldMotionBlur0x18 = (this._io.readF4be()) as any
      this.worldSaturation0x1c = (this._io.readF4be()) as any
      this.unkEnum0x20 = (this._io.readU4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (36) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (4085824509) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    carMotionBlur0x10: number;
    worldColourCubeWeight0x14: number;
    worldMotionBlur0x18: number;
    worldSaturation0x1c: number;

    /**
     * enum; 00_00_30_35_1
     */
    unkEnum0x20: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenEnvironmentKeyframeSky {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.rwMathVpuVector40x10 = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
      this.gameChangerId0x20 = (this._io.readU4be()) as any
      this.float32T0x24 = (this._io.readF4be()) as any
      this.float32T0x28 = (this._io.readF4be()) as any
      this.float32T0x2c = (this._io.readF4be()) as any
      this.float32T0x30 = (this._io.readF4be()) as any
      this.float32T0x34 = (this._io.readF4be()) as any
      this.float32T0x38 = (this._io.readF4be()) as any
      this.float32T0x3c = (this._io.readF4be()) as any
      this.float32T0x40 = (this._io.readF4be()) as any
      this.float32T0x44 = (this._io.readF4be()) as any
      this.ptrArrFloat32T0x48 = (this._io.readU4be()) as any
      this.float32T0x4c = (this._io.readF4be()) as any
      this.float32T0x50 = (this._io.readF4be()) as any
      this.float32T0x54 = (this._io.readF4be()) as any
      this.float32T0x58 = (this._io.readF4be()) as any
      this.float32T0x5c = (this._io.readF4be()) as any
      this.float32T0x60 = (this._io.readF4be()) as any
      this.float32T0x64 = (this._io.readF4be()) as any
      this.arrayCountFor0x48 = (this._io.readU2be()) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _instFloat32T0x48: Array<number | undefined> | undefined;
    get instFloat32T0x48(): Array<number | undefined> | undefined {
      if (typeof this._instFloat32T0x48 !== 'undefined')
        return this._instFloat32T0x48;
      if ((this.ptrArrFloat32T0x48 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrFloat32T0x48 as any));
        this._instFloat32T0x48 = [];
        for (let i = 0; i < (this.arrayCountFor0x48 as any); i++) {
          this._instFloat32T0x48.push(this._io.readF4be());
        }
        this._io.seek(_pos);
      }
      return this._instFloat32T0x48;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (108) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3450467609) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    rwMathVpuVector40x10: GenericGenObject.RwMathVpuVector4;
    gameChangerId0x20: number;
    float32T0x24: number;
    float32T0x28: number;
    float32T0x2c: number;
    float32T0x30: number;
    float32T0x34: number;
    float32T0x38: number;
    float32T0x3c: number;
    float32T0x40: number;
    float32T0x44: number;
    ptrArrFloat32T0x48: number;
    float32T0x4c: number;
    float32T0x50: number;
    float32T0x54: number;
    float32T0x58: number;
    float32T0x5c: number;
    float32T0x60: number;
    float32T0x64: number;
    arrayCountFor0x48: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenGameRule {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (16) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (494037508) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
  }
}

export namespace GenericGenObject {
  export class T000031D2 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenWcremoveWorldEntityBehaviour {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenBehaviour(this._io, this, this._root)) as any
      this.float32T0x1c = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (32) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1055028229) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenBehaviour;
    float32T0x1c: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenGameplayTriggerOutputSequenceOutput {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.sequence0x10 = (this._io.readU4be()) as any
      this.sequenceType0x14 = (this._io.readU4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (24) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3174528889) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    sequence0x10: number;

    /**
     * enum; 00_06_cc_77_1
     */
    sequenceType0x14: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenCarSelectData {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.copIdleSequences0xc = (this._io.readU1()) as any
      this.copSequences0x28 = (this._io.readU1()) as any
      this.racerIdleSequences0x44 = (this._io.readU1()) as any
      this.racerSequences0x60 = (this._io.readU1()) as any
      this.ptrArrCopPlacements0x7c = (this._io.readU4be()) as any
      this.gameChangerId0x80 = (this._io.readU4be()) as any
      this.ptrArrRacerPlacements0x84 = (this._io.readU4be()) as any
      this.uimemoryLimit0x88 = (this._io.readF4be()) as any
      this.uiresourceLimit0x8c = (this._io.readS4be()) as any
      this.arrayCountFor0x7c = (this._io.readU2be()) as any
      this.arrayCountFor0x84 = (this._io.readU2be()) as any
      this.loopSequences0x94 = (this._io.readU1()) as any
      this.splitByTier0x95 = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _instCopPlacements0x7c: Array<number | undefined> | undefined;
    get instCopPlacements0x7c(): Array<number | undefined> | undefined {
      if (typeof this._instCopPlacements0x7c !== 'undefined')
        return this._instCopPlacements0x7c;
      if ((this.ptrArrCopPlacements0x7c as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrCopPlacements0x7c as any));
        this._instCopPlacements0x7c = [];
        for (let i = 0; i < (this.arrayCountFor0x7c as any); i++) {
          this._instCopPlacements0x7c.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._instCopPlacements0x7c;
    }

    private _instRacerPlacements0x84: Array<number | undefined> | undefined;
    get instRacerPlacements0x84(): Array<number | undefined> | undefined {
      if (typeof this._instRacerPlacements0x84 !== 'undefined')
        return this._instRacerPlacements0x84;
      if ((this.ptrArrRacerPlacements0x84 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrRacerPlacements0x84 as any));
        this._instRacerPlacements0x84 = [];
        for (let i = 0; i < (this.arrayCountFor0x84 as any); i++) {
          this._instRacerPlacements0x84.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._instRacerPlacements0x84;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (152) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (4000545794) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;

    /**
     * enum; 00_00_32_82_1
     */
    copIdleSequences0xc: number;

    /**
     * enum; 00_00_32_82_1
     */
    copSequences0x28: number;

    /**
     * enum; 00_00_32_82_1
     */
    racerIdleSequences0x44: number;

    /**
     * enum; 00_00_32_82_1
     */
    racerSequences0x60: number;
    ptrArrCopPlacements0x7c: number;
    gameChangerId0x80: number;
    ptrArrRacerPlacements0x84: number;
    uimemoryLimit0x88: number;
    uiresourceLimit0x8c: number;

    /**
     * "CopPlacementsCount"
     */
    arrayCountFor0x7c: number;

    /**
     * "RacerPlacementsCount"
     */
    arrayCountFor0x84: number;
    loopSequences0x94: number;
    splitByTier0x95: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenPhysicalExplosionRaceCarOnGroundExplosion {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.float32T0x10 = (this._io.readF4be()) as any
      this.float32T0x14 = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (24) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3314905645) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    float32T0x10: number;
    float32T0x14: number;
  }
}

export namespace GenericGenObject {
  export class T0003F850 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenUielementMask {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.cgsCoreUniqueId0x10 = (this._io.readU4be()) as any
      this.ptrGenesysGenUielementBase0x14 = (this._io.readU4be()) as any
      this.bool8T0x18 = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(3)) as any
    }

    private _instGenesysGenUielementBase0x14: GenericGenObject.GenesysGenUielementBase | undefined;
    get instGenesysGenUielementBase0x14(): GenericGenObject.GenesysGenUielementBase | undefined {
      if (typeof this._instGenesysGenUielementBase0x14 !== 'undefined')
        return this._instGenesysGenUielementBase0x14;
      if ((this.ptrGenesysGenUielementBase0x14 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrGenesysGenUielementBase0x14 as any));
        this._instGenesysGenUielementBase0x14 = (new GenericGenObject.GenesysGenUielementBase(this._io, this, this._root)) as any
        this._io.seek(_pos);
      }
      return this._instGenesysGenUielementBase0x14;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (28) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (619283814) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    cgsCoreUniqueId0x10: number;
    ptrGenesysGenUielementBase0x14: number;
    bool8T0x18: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class T4099F3Ac {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenSoundDistanceFalloff {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.curveType0x10 = (this._io.readF4be()) as any
      this.curveTypeReverb0x14 = (this._io.readF4be()) as any
      this.divergenceAtMaxDistance0x18 = (this._io.readF4be()) as any
      this.divergenceAtMinDistance0x1c = (this._io.readF4be()) as any
      this.float32T0x20 = (this._io.readF4be()) as any
      this.float32T0x24 = (this._io.readF4be()) as any
      this.float32T0x28 = (this._io.readF4be()) as any
      this.float32T0x2c = (this._io.readF4be()) as any
      this.maxDistance0x30 = (this._io.readF4be()) as any
      this.maxDistanceDivergence0x34 = (this._io.readF4be()) as any
      this.maxDistanceReverb0x38 = (this._io.readF4be()) as any
      this.minDistance0x3c = (this._io.readF4be()) as any
      this.minDistanceDivergence0x40 = (this._io.readF4be()) as any
      this.minDistanceReverb0x44 = (this._io.readF4be()) as any
      this.bool8T0x48 = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(3)) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (76) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (174014684) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    curveType0x10: number;
    curveTypeReverb0x14: number;
    divergenceAtMaxDistance0x18: number;
    divergenceAtMinDistance0x1c: number;
    float32T0x20: number;
    float32T0x24: number;
    float32T0x28: number;
    float32T0x2c: number;
    maxDistance0x30: number;
    maxDistanceDivergence0x34: number;
    maxDistanceReverb0x38: number;
    minDistance0x3c: number;
    minDistanceDivergence0x40: number;
    minDistanceReverb0x44: number;
    bool8T0x48: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenNitrousEarningGameRule {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenGameRule(this._io, this, this._root)) as any
      this.float32T0x10 = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (20) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2358324053) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenGameRule;
    float32T0x10: number;
  }
}

export namespace GenericGenObject {
  export class T35A6061e {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class T00003035 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class F7FfD1F8 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class T00003027 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenEvent {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.ptrArrAutotestCheckpoints0xc = (this._io.readU4be()) as any
      this.gameChangerId0x10 = (this._io.readU4be()) as any
      this.gameMode0x14 = (this._io.readU4be()) as any
      this.cycleTimeOfDay0x18 = (this._io.readF4be()) as any
      this.finishTimeOfDay0x1c = (this._io.readF4be()) as any
      this.sunDirection0x20 = (this._io.readF4be()) as any
      this.timeOfDay0x24 = (this._io.readF4be()) as any
      this.arrayCountFor0xc = (this._io.readU2be()) as any
      this.isAlternativeWeather0x2a = (this._io.readU1()) as any
      this.isRainActive0x2b = (this._io.readU1()) as any
      this.isThunderActive0x2c = (this._io.readU1()) as any
      this.bool8T0x2d = (this._io.readU1()) as any
      this.overrideSunDirection0x2e = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(1)) as any
    }

    private _instAutotestCheckpoints0xc: Array<number | undefined> | undefined;
    get instAutotestCheckpoints0xc(): Array<number | undefined> | undefined {
      if (typeof this._instAutotestCheckpoints0xc !== 'undefined')
        return this._instAutotestCheckpoints0xc;
      if ((this.ptrArrAutotestCheckpoints0xc as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrAutotestCheckpoints0xc as any));
        this._instAutotestCheckpoints0xc = [];
        for (let i = 0; i < (this.arrayCountFor0xc as any); i++) {
          this._instAutotestCheckpoints0xc.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._instAutotestCheckpoints0xc;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (48) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1762060451) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    ptrArrAutotestCheckpoints0xc: number;
    gameChangerId0x10: number;
    gameMode0x14: number;
    cycleTimeOfDay0x18: number;
    finishTimeOfDay0x1c: number;
    sunDirection0x20: number;
    timeOfDay0x24: number;

    /**
     * "AutotestCheckpointsCount"
     */
    arrayCountFor0xc: number;
    isAlternativeWeather0x2a: number;
    isRainActive0x2b: number;
    isThunderActive0x2c: number;
    bool8T0x2d: number;
    overrideSunDirection0x2e: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class T0003F3C4 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class A76d0e28 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class CgsCoreUniqueId {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenEnvironmentKeyframeVfx {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.float32T0x10 = (this._io.readF4be()) as any
      this.float32T0x14 = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (24) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1150238934) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    float32T0x10: number;
    float32T0x14: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenAiplayerType {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.rollout0x10 = (this._io.readU4be()) as any
      this.aggressionDelay0x14 = (this._io.readF4be()) as any
      this.aggressionFrequency0x18 = (this._io.readF4be()) as any
      this.float32T0x1c = (this._io.readF4be()) as any
      this.escapingSpeed0x20 = (this._io.readF4be()) as any
      this.failJumpDazeTime0x24 = (this._io.readF4be()) as any
      this.flatOutInitialTime0x28 = (this._io.readF4be()) as any
      this.flatOutTime0x2c = (this._io.readF4be()) as any
      this.hitDamagePercentageToDaze0x30 = (this._io.readF4be()) as any
      this.hitDazeTime0x34 = (this._io.readF4be()) as any
      this.maxDamageForSpeedEffect0x38 = (this._io.readF4be()) as any
      this.maxEventBalancingDistance0x3c = (this._io.readF4be()) as any
      this.float32T0x40 = (this._io.readF4be()) as any
      this.minDamageForSpeedEffect0x44 = (this._io.readF4be()) as any
      this.minEventBalancingDistance0x48 = (this._io.readF4be()) as any
      this.minShortcutTime0x4c = (this._io.readF4be()) as any
      this.minThrottleDamagePercent0x50 = (this._io.readF4be()) as any
      this.float32T0x54 = (this._io.readF4be()) as any
      this.shortcutTakingPercentage0x58 = (this._io.readF4be()) as any
      this.speed0x5c = (this._io.readF4be()) as any
      this.speedMatchingMaxDistance0x60 = (this._io.readF4be()) as any
      this.speedMatchingMaxSpeed0x64 = (this._io.readF4be()) as any
      this.speedMatchingMinSpeed0x68 = (this._io.readF4be()) as any
      this.speedMatchingSpeedDifference0x6c = (this._io.readF4be()) as any
      this.toughness0x70 = (this._io.readF4be()) as any
      this.turnAtJunctionPercentage0x74 = (this._io.readF4be()) as any
      this.uturnMinTime0x78 = (this._io.readF4be()) as any
      this.weaponAvoidancePercentage0x7c = (this._io.readF4be()) as any
      this.weavingDuration0x80 = (this._io.readF4be()) as any
      this.weavingFrequency0x84 = (this._io.readF4be()) as any
      this.aggressionType0x88 = (this._io.readU2be()) as any
      this.behaviour0x8a = (this._io.readU2be()) as any
      this.nitrousUsage0x8c = (this._io.readU2be()) as any
      this.weavingType0x8e = (this._io.readU2be()) as any
      this.canRhino0x90 = (this._io.readU1()) as any
      this.doUturns0x91 = (this._io.readU1()) as any
      this.isCop0x92 = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(1)) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (148) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2152868223) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    rollout0x10: number;
    aggressionDelay0x14: number;
    aggressionFrequency0x18: number;
    float32T0x1c: number;
    escapingSpeed0x20: number;
    failJumpDazeTime0x24: number;
    flatOutInitialTime0x28: number;
    flatOutTime0x2c: number;
    hitDamagePercentageToDaze0x30: number;
    hitDazeTime0x34: number;
    maxDamageForSpeedEffect0x38: number;
    maxEventBalancingDistance0x3c: number;
    float32T0x40: number;
    minDamageForSpeedEffect0x44: number;
    minEventBalancingDistance0x48: number;
    minShortcutTime0x4c: number;
    minThrottleDamagePercent0x50: number;
    float32T0x54: number;
    shortcutTakingPercentage0x58: number;
    speed0x5c: number;
    speedMatchingMaxDistance0x60: number;
    speedMatchingMaxSpeed0x64: number;
    speedMatchingMinSpeed0x68: number;
    speedMatchingSpeedDifference0x6c: number;
    toughness0x70: number;
    turnAtJunctionPercentage0x74: number;
    uturnMinTime0x78: number;
    weaponAvoidancePercentage0x7c: number;
    weavingDuration0x80: number;
    weavingFrequency0x84: number;

    /**
     * enum; 00_06_fa_71_1
     */
    aggressionType0x88: number;

    /**
     * enum; 00_05_f6_43_1
     */
    behaviour0x8a: number;

    /**
     * enum; 00_06_fa_8a_1
     */
    nitrousUsage0x8c: number;

    /**
     * enum; 00_06_fa_70_1
     */
    weavingType0x8e: number;
    canRhino0x90: number;
    doUturns0x91: number;
    isCop0x92: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class Ptr {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: unknown | undefined,
      readonly _root: GenericGenObject | undefined,
      dtype: string,
    ) {
      this.dtype = dtype;

      this._read();
    }

    _read() {
      this.offset = (this._io.readS4be()) as any
    }

    private _data: GenericGenObject.Atype | undefined;
    get data(): GenericGenObject.Atype | undefined {
      if (typeof this._data !== 'undefined')
        return this._data;
      if ((this.offset as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.offset as any));
        this._data = (new GenericGenObject.Atype(this._io, this, this._root, (this.dtype as any))) as any
        this._io.seek(_pos);
      }
      return this._data;
    }

    offset: number;
    dtype: string;
  }
}

export namespace GenericGenObject {
  export class Int32T {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class T0000301d {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenSpeedbreakerWeapon {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenWeapon(this._io, this, this._root)) as any
      this.float32T0xb0 = (this._io.readF4be()) as any
      this.float32T0xb4 = (this._io.readF4be()) as any
      this.float32T0xb8 = (this._io.readF4be()) as any
      this.float32T0xbc = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (192) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3548375797) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenWeapon;
    float32T0xb0: number;
    float32T0xb4: number;
    float32T0xb8: number;
    float32T0xbc: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenGameModeScoreOverride {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.cgsCoreUniqueId0x10 = (this._io.readU4be()) as any
      this.score0x14 = (this._io.readS4be()) as any
      this.int32T0x18 = (this._io.readS4be()) as any
      this.xp0x1c = (this._io.readS4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (32) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3763436769) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    cgsCoreUniqueId0x10: number;
    score0x14: number;
    int32T0x18: number;
    xp0x1c: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenUielementPrototypeImage {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.cgsCoreStringBase0xc = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.gameChangerId0x14 = (this._io.readU4be()) as any
      this.cgsCoreUniqueId0x18 = (this._io.readU4be()) as any
      this.unkEnum0x1c = (this._io.readU4be()) as any
      this.ptrTint0x20 = (this._io.readU4be()) as any
      this.ptrGenesysGenUielementBase0x24 = (this._io.readU4be()) as any
      this.bool8T0x28 = (this._io.readU1()) as any
      this.bool8T0x29 = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _instTint0x20: number | undefined;
    get instTint0x20(): number | undefined {
      if (typeof this._instTint0x20 !== 'undefined')
        return this._instTint0x20;
      if ((this.ptrTint0x20 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrTint0x20 as any));
        this._instTint0x20 = (this._io.readU4be()) as any
        this._io.seek(_pos);
      }
      return this._instTint0x20;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (44) as any
      return this._size;
    }

    private _instGenesysGenUielementBase0x24: GenericGenObject.GenesysGenUielementBase | undefined;
    get instGenesysGenUielementBase0x24(): GenericGenObject.GenesysGenUielementBase | undefined {
      if (typeof this._instGenesysGenUielementBase0x24 !== 'undefined')
        return this._instGenesysGenUielementBase0x24;
      if ((this.ptrGenesysGenUielementBase0x24 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrGenesysGenUielementBase0x24 as any));
        this._instGenesysGenUielementBase0x24 = (new GenericGenObject.GenesysGenUielementBase(this._io, this, this._root)) as any
        this._io.seek(_pos);
      }
      return this._instGenesysGenUielementBase0x24;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3128949721) as any
      return this._muVersionHash;
    }

    private _inst00002a83120x1c: number | undefined;
    get inst00002a83120x1c(): number | undefined {
      if (typeof this._inst00002a83120x1c !== 'undefined')
        return this._inst00002a83120x1c;
      if ((this.unkEnum0x1c as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.unkEnum0x1c as any));
        this._inst00002a83120x1c = (this._io.readU4be()) as any
        this._io.seek(_pos);
      }
      return this._inst00002a83120x1c;
    }

    baseObject: GenericGenObject.GenObj;
    cgsCoreStringBase0xc: GenericGenObject.StringBase;
    gameChangerId0x14: number;
    cgsCoreUniqueId0x18: number;

    /**
     * enum; 00_00_2a_83_1_2
     */
    unkEnum0x1c: number;

    /**
     * enum; 00_00_2a_83_1_1
     */
    ptrTint0x20: number;
    ptrGenesysGenUielementBase0x24: number;
    bool8T0x28: number;
    bool8T0x29: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenUielementPrototypeImageTintProperties {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.value0x10 = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
      this.binding0x20 = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.cgsCoreStringBase0x28 = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.gameChangerId0x30 = (this._io.readU4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (52) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1079751127) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    value0x10: GenericGenObject.RwMathVpuVector4;
    binding0x20: GenericGenObject.StringBase;
    cgsCoreStringBase0x28: GenericGenObject.StringBase;
    gameChangerId0x30: number;
  }
}

export namespace GenericGenObject {
  export class T0003F715 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenThermalVisionMode {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenVisionMode(this._io, this, this._root)) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (172) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1304174185) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenVisionMode;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenSearchlightBehaviour {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenBehaviour(this._io, this, this._root)) as any
      this.cgsResourceHandle0x1c = (this._io.readBytes(8)) as any
      this.cgsResourceHandle0x24 = (this._io.readBytes(8)) as any
      this.lightDefinition0x2c = (this._io.readBytes(8)) as any
      this.locatorGroup0x34 = (this._io.readU4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (56) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2557796749) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenBehaviour;
    cgsResourceHandle0x1c: Uint8Array;
    cgsResourceHandle0x24: Uint8Array;
    lightDefinition0x2c: Uint8Array;
    locatorGroup0x34: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenStoreItem {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.name0xc = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.psnpackageName0x14 = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.nucleusEntTag0x1c = (this._io.readBytes(8)) as any
      this.gameChangerId0x24 = (this._io.readU4be()) as any
      this.ptrArrLongDescription0x28 = (this._io.readU4be()) as any
      this.mainImage0x2c = (this._io.readU4be()) as any
      this.subImage10x30 = (this._io.readU4be()) as any
      this.subImage20x34 = (this._io.readU4be()) as any
      this.title0x38 = (this._io.readU4be()) as any
      this.ptrArrEntitlements0x3c = (this._io.readU4be()) as any
      this.x360licenseMask0x40 = (this._io.readS4be()) as any
      this.x360offerId0x44 = (this._io.readS4be()) as any
      this.arrayCountFor0x3c = (this._io.readU2be()) as any
      this.arrayCountFor0x28 = (this._io.readU2be()) as any
      this.showInStore0x4c = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(3)) as any
    }

    private _instLongDescription0x28: Array<number | undefined> | undefined;
    get instLongDescription0x28(): Array<number | undefined> | undefined {
      if (typeof this._instLongDescription0x28 !== 'undefined')
        return this._instLongDescription0x28;
      if ((this.ptrArrLongDescription0x28 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrLongDescription0x28 as any));
        this._instLongDescription0x28 = [];
        for (let i = 0; i < (this.arrayCountFor0x28 as any); i++) {
          this._instLongDescription0x28.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._instLongDescription0x28;
    }

    private _instEntitlements0x3c: Array<GenericGenObject.CgsResourceHandle | undefined> | undefined;
    get instEntitlements0x3c(): Array<GenericGenObject.CgsResourceHandle | undefined> | undefined {
      if (typeof this._instEntitlements0x3c !== 'undefined')
        return this._instEntitlements0x3c;
      if ((this.ptrArrEntitlements0x3c as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrEntitlements0x3c as any));
        this._instEntitlements0x3c = [];
        for (let i = 0; i < (this.arrayCountFor0x3c as any); i++) {
          this._instEntitlements0x3c.push(new GenericGenObject.CgsResourceHandle(this._io, this, this._root));
        }
        this._io.seek(_pos);
      }
      return this._instEntitlements0x3c;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (80) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2947788458) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    name0xc: GenericGenObject.StringBase;
    psnpackageName0x14: GenericGenObject.StringBase;
    nucleusEntTag0x1c: Uint8Array;
    gameChangerId0x24: number;
    ptrArrLongDescription0x28: number;
    mainImage0x2c: number;
    subImage10x30: number;
    subImage20x34: number;
    title0x38: number;
    ptrArrEntitlements0x3c: number;
    x360licenseMask0x40: number;
    x360offerId0x44: number;

    /**
     * "EntitlementsCount"
     */
    arrayCountFor0x3c: number;

    /**
     * "Long_DescriptionCount"
     */
    arrayCountFor0x28: number;
    showInStore0x4c: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenJumpTimelineController {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenSequenceTimelineController(this._io, this, this._root)) as any
      this.destinationTime0x1c = (this._io.readF4be()) as any
      this.triggerTime0x20 = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (36) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (115778840) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenSequenceTimelineController;
    destinationTime0x1c: number;
    triggerTime0x20: number;
  }
}

export namespace GenericGenObject {
  export class T8e7d5f21 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenRoadBlockLayerItem {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.cgsCoreUniqueId0x10 = (this._io.readU4be()) as any
      this.angle0x14 = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (24) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2808391399) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    cgsCoreUniqueId0x10: number;
    angle0x14: number;
  }
}

export namespace GenericGenObject {
  export class RwRgba {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.arrInlineUint8T0x0 = [];
      for (let i = 0; i < 4; i++) {
        this.arrInlineUint8T0x0.push(this._io.readU1());
      }
      this.padding = (this._io.readBytes(3)) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (4) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (185604263) as any
      return this._muVersionHash;
    }

    arrInlineUint8T0x0: Array<number>;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenEnvironmentTimelineTimelineKeyframe {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.cgsResourceHandle0xc = (this._io.readBytes(8)) as any
      this.gameChangerId0x14 = (this._io.readU4be()) as any
      this.timeOfDay0x18 = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (28) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (4341541) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    cgsResourceHandle0xc: Uint8Array;
    gameChangerId0x14: number;
    timeOfDay0x18: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenUielementScrollableLabelTextProperties {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.rwMathVpuVector40x10 = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
      this.cgsCoreStringBase0x20 = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.cgsResourceHandle0x28 = (this._io.readBytes(8)) as any
      this.gameChangerId0x30 = (this._io.readU4be()) as any
      this.unoO0x34 = (this._io.readU2be()) as any
      this.bool8T0x36 = (this._io.readU1()) as any
      this.bool8T0x37 = (this._io.readU1()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (56) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1094276132) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    rwMathVpuVector40x10: GenericGenObject.RwMathVpuVector4;
    cgsCoreStringBase0x20: GenericGenObject.StringBase;
    cgsResourceHandle0x28: Uint8Array;
    gameChangerId0x30: number;

    /**
     * enum; 35_a6_06_1e
     */
    unoO0x34: number;
    bool8T0x36: number;
    bool8T0x37: number;
  }
}

export namespace GenericGenObject {
  export class T000031C4 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenMixerChannelPriority {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.priority0xc = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(3)) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (16) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2235129779) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    priority0xc: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenEnvironmentTimelineSequenceItem {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenSequenceItem(this._io, this, this._root)) as any
      this.cgsResourceHandle0x20 = (this._io.readBytes(8)) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (36) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2293547115) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenSequenceItem;
    cgsResourceHandle0x20: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenPhysicalDefinitionRigidBodyConvexHullVolume {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.volumeToBodyTransform0x10 = (new GenericGenObject.RwMathVpuMatrix44affine(this._io, this, this._root)) as any
      this.convexHull0x50 = (this._io.readBytes(8)) as any
      this.gameChangerId0x58 = (this._io.readU4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (92) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1664340785) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    volumeToBodyTransform0x10: GenericGenObject.RwMathVpuMatrix44affine;
    convexHull0x50: Uint8Array;
    gameChangerId0x58: number;
  }
}

export namespace GenericGenObject {
  export class FfFfFfF8 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.ptrArrPtrItem0x10 = (this._io.readU4be()) as any
      this.arrayCountFor0x10 = (this._io.readU2be()) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _instItem0x10: Array<GenericGenObject.Ptr | undefined> | undefined;

    /**
     * 'instance of Genesys.Object'
     */
    get instItem0x10(): Array<GenericGenObject.Ptr | undefined> | undefined {
      if (typeof this._instItem0x10 !== 'undefined')
        return this._instItem0x10;
      if ((this.ptrArrPtrItem0x10 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrPtrItem0x10 as any));
        this._instItem0x10 = [];
        for (let i = 0; i < (this.arrayCountFor0x10 as any); i++) {
          this._instItem0x10.push(new GenericGenObject.Ptr(this._io, this, this._root, "generic_gen_object"));
        }
        this._io.seek(_pos);
      }
      return this._instItem0x10;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (24) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3162856831) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    ptrArrPtrItem0x10: number;

    /**
     * "ItemCount"
     */
    arrayCountFor0x10: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class T0006Cc2f {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenPhysicalDefinitionRigidBodyBoxVolume {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.volumeToBodyTransform0x10 = (new GenericGenObject.RwMathVpuMatrix44affine(this._io, this, this._root)) as any
      this.halfsize0x50 = (new GenericGenObject.RwMathVpuVector3(this._io, this, this._root)) as any
      this.gameChangerId0x60 = (this._io.readU4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (100) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2630734184) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    volumeToBodyTransform0x10: GenericGenObject.RwMathVpuMatrix44affine;
    halfsize0x50: GenericGenObject.RwMathVpuVector3;
    gameChangerId0x60: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenGrenadeWeapon {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenWeapon(this._io, this, this._root)) as any
      this.cgsResourceHandle0xb0 = (this._io.readBytes(8)) as any
      this.float32T0xb8 = (this._io.readF4be()) as any
      this.float32T0xbc = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (192) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2687264588) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenWeapon;
    cgsResourceHandle0xb0: Uint8Array;
    float32T0xb8: number;
    float32T0xbc: number;
  }
}

export namespace GenericGenObject {
  export class T0003F65b {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenWeaponUpgrade {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.description0xc = (this._io.readU4be()) as any
      this.gameChangerId0x10 = (this._io.readU4be()) as any
      this.image0x14 = (this._io.readU4be()) as any
      this.name0x18 = (this._io.readU4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (28) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (887880830) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    description0xc: number;
    gameChangerId0x10: number;
    image0x14: number;
    name0x18: number;
  }
}

export namespace GenericGenObject {
  export class GenesysObject {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenUielementPrototypeShape {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.rwMathVpuVector40x10 = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
      this.gameChangerId0x20 = (this._io.readU4be()) as any
      this.ptrGenesysGenUielementBase0x24 = (this._io.readU4be()) as any
      this.int32T0x28 = (this._io.readS4be()) as any
      this.unkEnum0x2c = (this._io.readU4be()) as any
    }

    private _instGenesysGenUielementBase0x24: GenericGenObject.GenesysGenUielementBase | undefined;
    get instGenesysGenUielementBase0x24(): GenericGenObject.GenesysGenUielementBase | undefined {
      if (typeof this._instGenesysGenUielementBase0x24 !== 'undefined')
        return this._instGenesysGenUielementBase0x24;
      if ((this.ptrGenesysGenUielementBase0x24 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrGenesysGenUielementBase0x24 as any));
        this._instGenesysGenUielementBase0x24 = (new GenericGenObject.GenesysGenUielementBase(this._io, this, this._root)) as any
        this._io.seek(_pos);
      }
      return this._instGenesysGenUielementBase0x24;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (48) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (394486533) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    rwMathVpuVector40x10: GenericGenObject.RwMathVpuVector4;
    gameChangerId0x20: number;
    ptrGenesysGenUielementBase0x24: number;
    int32T0x28: number;

    /**
     * enum; d7_b2_21_da
     */
    unkEnum0x2c: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenUielementPrototypeScrollingText {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.cgsCoreStringBase0xc = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.gameChangerId0x14 = (this._io.readU4be()) as any
      this.unkEnum0x18 = (this._io.readU4be()) as any
      this.unkEnum0x1c = (this._io.readU4be()) as any
      this.ptrGenesysGenUielementBase0x20 = (this._io.readU4be()) as any
      this.int32T0x24 = (this._io.readS4be()) as any
      this.int32T0x28 = (this._io.readS4be()) as any
      this.arrayCountFor0x18 = (this._io.readU2be()) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _instGenesysGenUielementBase0x20: GenericGenObject.GenesysGenUielementBase | undefined;
    get instGenesysGenUielementBase0x20(): GenericGenObject.GenesysGenUielementBase | undefined {
      if (typeof this._instGenesysGenUielementBase0x20 !== 'undefined')
        return this._instGenesysGenUielementBase0x20;
      if ((this.ptrGenesysGenUielementBase0x20 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrGenesysGenUielementBase0x20 as any));
        this._instGenesysGenUielementBase0x20 = (new GenericGenObject.GenesysGenUielementBase(this._io, this, this._root)) as any
        this._io.seek(_pos);
      }
      return this._instGenesysGenUielementBase0x20;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (48) as any
      return this._size;
    }

    private _inst00002a85120x1c: number | undefined;
    get inst00002a85120x1c(): number | undefined {
      if (typeof this._inst00002a85120x1c !== 'undefined')
        return this._inst00002a85120x1c;
      if ((this.unkEnum0x1c as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.unkEnum0x1c as any));
        this._inst00002a85120x1c = (this._io.readU4be()) as any
        this._io.seek(_pos);
      }
      return this._inst00002a85120x1c;
    }

    private _inst00002a85110x18: Array<number | undefined> | undefined;
    get inst00002a85110x18(): Array<number | undefined> | undefined {
      if (typeof this._inst00002a85110x18 !== 'undefined')
        return this._inst00002a85110x18;
      if ((this.unkEnum0x18 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.unkEnum0x18 as any));
        this._inst00002a85110x18 = [];
        for (let i = 0; i < (this.arrayCountFor0x18 as any); i++) {
          this._inst00002a85110x18.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._inst00002a85110x18;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3431394552) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    cgsCoreStringBase0xc: GenericGenObject.StringBase;
    gameChangerId0x14: number;

    /**
     * enum; 00_00_2a_85_1_1
     */
    unkEnum0x18: number;

    /**
     * enum; 00_00_2a_85_1_2
     */
    unkEnum0x1c: number;
    ptrGenesysGenUielementBase0x20: number;
    int32T0x24: number;
    int32T0x28: number;
    arrayCountFor0x18: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class Uint16T {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class T0003F6D5 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenGameUnlockList {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.ptrArrPtrItem0x10 = (this._io.readU4be()) as any
      this.arrayCountFor0x10 = (this._io.readU2be()) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _instItem0x10: Array<GenericGenObject.Ptr | undefined> | undefined;

    /**
     * 'instance of Genesys.Object'
     */
    get instItem0x10(): Array<GenericGenObject.Ptr | undefined> | undefined {
      if (typeof this._instItem0x10 !== 'undefined')
        return this._instItem0x10;
      if ((this.ptrArrPtrItem0x10 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrPtrItem0x10 as any));
        this._instItem0x10 = [];
        for (let i = 0; i < (this.arrayCountFor0x10 as any); i++) {
          this._instItem0x10.push(new GenericGenObject.Ptr(this._io, this, this._root, "generic_gen_object"));
        }
        this._io.seek(_pos);
      }
      return this._instItem0x10;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (24) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (738476701) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    ptrArrPtrItem0x10: number;

    /**
     * "ItemCount"
     */
    arrayCountFor0x10: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenCoronaGlow {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.colour0x10 = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
      this.arrInlineFloat32T0x20 = [];
      for (let i = 0; i < 6; i++) {
        this.arrInlineFloat32T0x20.push(this._io.readF4be());
      }
      this.arrInlineFloat32T0x38 = [];
      for (let i = 0; i < 6; i++) {
        this.arrInlineFloat32T0x38.push(this._io.readF4be());
      }
      this.material0x50 = (this._io.readBytes(8)) as any
      this.gameChangerId0x58 = (this._io.readU4be()) as any
      this.brightness0x5c = (this._io.readF4be()) as any
      this.depthBias0x60 = (this._io.readF4be()) as any
      this.float32T0x64 = (this._io.readF4be()) as any
      this.float32T0x68 = (this._io.readF4be()) as any
      this.rotationOffset0x6c = (this._io.readF4be()) as any
      this.arrayCountFor0x20 = (this._io.readU2be()) as any
      this.arrayCountFor0x38 = (this._io.readU2be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (116) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3106938524) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    colour0x10: GenericGenObject.RwMathVpuVector4;
    arrInlineFloat32T0x20: Array<number>;
    arrInlineFloat32T0x38: Array<number>;
    material0x50: Uint8Array;
    gameChangerId0x58: number;
    brightness0x5c: number;
    depthBias0x60: number;
    float32T0x64: number;
    float32T0x68: number;
    rotationOffset0x6c: number;
    arrayCountFor0x20: number;
    arrayCountFor0x38: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenGameplayTrigger {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.predicate0xc = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.gameChangerId0x14 = (this._io.readU4be()) as any
      this.timeToWait0x18 = (this._io.readF4be()) as any
      this.ptrArrInput0x1c = (this._io.readU4be()) as any
      this.ptrArrOutput0x20 = (this._io.readU4be()) as any
      this.triggerLifetime0x24 = (this._io.readU2be()) as any
      this.arrayCountFor0x1c = (this._io.readU2be()) as any
      this.arrayCountFor0x20 = (this._io.readU2be()) as any
      this.addToMiniMap0x2a = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(1)) as any
    }

    private _instInput0x1c: Array<number | undefined> | undefined;
    get instInput0x1c(): Array<number | undefined> | undefined {
      if (typeof this._instInput0x1c !== 'undefined')
        return this._instInput0x1c;
      if ((this.ptrArrInput0x1c as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrInput0x1c as any));
        this._instInput0x1c = [];
        for (let i = 0; i < (this.arrayCountFor0x1c as any); i++) {
          this._instInput0x1c.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._instInput0x1c;
    }

    private _instOutput0x20: Array<number | undefined> | undefined;
    get instOutput0x20(): Array<number | undefined> | undefined {
      if (typeof this._instOutput0x20 !== 'undefined')
        return this._instOutput0x20;
      if ((this.ptrArrOutput0x20 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrOutput0x20 as any));
        this._instOutput0x20 = [];
        for (let i = 0; i < (this.arrayCountFor0x20 as any); i++) {
          this._instOutput0x20.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._instOutput0x20;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (44) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (606894659) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    predicate0xc: GenericGenObject.StringBase;
    gameChangerId0x14: number;
    timeToWait0x18: number;

    /**
     * enum; 00_06_fb_3b_1
     */
    ptrArrInput0x1c: number;

    /**
     * enum; 00_06_fb_3c_1
     */
    ptrArrOutput0x20: number;

    /**
     * enum; 00_06_cc_72_1
     */
    triggerLifetime0x24: number;

    /**
     * "InputCount"
     */
    arrayCountFor0x1c: number;

    /**
     * "OutputCount"
     */
    arrayCountFor0x20: number;
    addToMiniMap0x2a: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class DaDc9b17 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenUielementBaseRenderingData {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.cgsResourceHandle0xc = (this._io.readBytes(8)) as any
      this.gameChangerId0x14 = (this._io.readU4be()) as any
      this.cgsCoreUniqueId0x18 = (this._io.readU4be()) as any
      this.ptrArrCgsResourceHandle0x1c = (this._io.readU4be()) as any
      this.arrayCountFor0x1c = (this._io.readU2be()) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _instCgsResourceHandle0x1c: Array<GenericGenObject.CgsResourceHandle | undefined> | undefined;
    get instCgsResourceHandle0x1c(): Array<GenericGenObject.CgsResourceHandle | undefined> | undefined {
      if (typeof this._instCgsResourceHandle0x1c !== 'undefined')
        return this._instCgsResourceHandle0x1c;
      if ((this.ptrArrCgsResourceHandle0x1c as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrCgsResourceHandle0x1c as any));
        this._instCgsResourceHandle0x1c = [];
        for (let i = 0; i < (this.arrayCountFor0x1c as any); i++) {
          this._instCgsResourceHandle0x1c.push(new GenericGenObject.CgsResourceHandle(this._io, this, this._root));
        }
        this._io.seek(_pos);
      }
      return this._instCgsResourceHandle0x1c;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (36) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (4158115530) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    cgsResourceHandle0xc: Uint8Array;
    gameChangerId0x14: number;
    cgsCoreUniqueId0x18: number;
    ptrArrCgsResourceHandle0x1c: number;
    arrayCountFor0x1c: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class T000031Ca {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenDustStormMinimapUpgrade {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenWeaponUpgrade(this._io, this, this._root)) as any
      this.float32T0x1c = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (32) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2327923899) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenWeaponUpgrade;
    float32T0x1c: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenPostFxsequenceItem {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenSequenceItem(this._io, this, this._root)) as any
      this.postFxstate0x20 = (this._io.readBytes(8)) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (36) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2580244534) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenSequenceItem;
    postFxstate0x20: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenUicolour {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.cgsCoreStringBase0xc = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
      this.gameChangerId0x14 = (this._io.readU4be()) as any
      this.colour0x18 = (new GenericGenObject.RwRgba(this._io, this, this._root)) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (28) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1057898069) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    cgsCoreStringBase0xc: GenericGenObject.StringBase;
    gameChangerId0x14: number;
    colour0x18: GenericGenObject.RwRgba;
  }
}

export namespace GenericGenObject {
  export class T0000303d {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenGameRank {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.rankName0x10 = (this._io.readU4be()) as any
      this.cgsCoreUniqueId0x14 = (this._io.readU4be()) as any
      this.rankNumber0x18 = (this._io.readS4be()) as any
      this.bool8T0x1c = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(3)) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (32) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1881019249) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    rankName0x10: number;
    cgsCoreUniqueId0x14: number;
    rankNumber0x18: number;
    bool8T0x1c: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class T96C15369 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenTextStyleTextStyleLocale {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.cgsCoreUniqueId0xc = (this._io.readU4be()) as any
      this.cgsCoreUniqueId0x10 = (this._io.readU4be()) as any
      this.gameChangerId0x14 = (this._io.readU4be()) as any
      this.float32T0x18 = (this._io.readF4be()) as any
      this.float32T0x1c = (this._io.readF4be()) as any
      this.float32T0x20 = (this._io.readF4be()) as any
      this.unkEnum0x24 = (this._io.readU4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (40) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (379456317) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    cgsCoreUniqueId0xc: number;
    cgsCoreUniqueId0x10: number;
    gameChangerId0x14: number;
    float32T0x18: number;
    float32T0x1c: number;
    float32T0x20: number;

    /**
     * enum; 95_95_0d_30
     */
    unkEnum0x24: number;
  }
}

export namespace GenericGenObject {
  export class CgsCoreStringBase {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.ofsArrBuffer0x0 = (this._io.readU4be()) as any
      this.arrayCountFor0x0 = (this._io.readU4be()) as any
    }

    private _instBuffer0x0: string | undefined;
    get instBuffer0x0(): string | undefined {
      if (typeof this._instBuffer0x0 !== 'undefined')
        return this._instBuffer0x0;
      if ((this.ofsArrBuffer0x0 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ofsArrBuffer0x0 as any));
        this._instBuffer0x0 = (KaitaiStream.bytesToStr(this._io.readBytes((this.arrayCountFor0x0 as any)), "ascii")) as any
        this._io.seek(_pos);
      }
      return this._instBuffer0x0;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (8) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2516314814) as any
      return this._muVersionHash;
    }

    ofsArrBuffer0x0: number;

    /**
     * "Capacity"
     */
    arrayCountFor0x0: number;
  }
}

export namespace GenericGenObject {
  export class GenesysObjCollection {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.unkId = (this._io.readU4be()) as any
      this.collectionStartOffset = (this._io.readU4be()) as any
      this.collectionCount = (this._io.readU2be()) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _objCollection: Array<GenericGenObject.Ptr>;
    get objCollection(): Array<GenericGenObject.Ptr> {
      if (typeof this._objCollection !== 'undefined')
        return this._objCollection;
      let _pos = this._io.pos;
      this._io.seek((this.collectionStartOffset as any));
      this._objCollection = [];
      for (let i = 0; i < (this.collectionCount as any); i++) {
        this._objCollection.push(new GenericGenObject.Ptr(this._io, this, this._root, "generic_gen_object"));
      }
      this._io.seek(_pos);
      return this._objCollection;
    }

    baseObject: GenericGenObject.GenObj;
    unkId: number;
    collectionStartOffset: number;
    collectionCount: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenEnvironmentKeyframeFog {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.colour0x10 = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
      this.gameChangerId0x20 = (this._io.readU4be()) as any
      this.float32T0x24 = (this._io.readF4be()) as any
      this.float32T0x28 = (this._io.readF4be()) as any
      this.float32T0x2c = (this._io.readF4be()) as any
      this.arrInlineFloat32T0x30 = [];
      for (let i = 0; i < 5; i++) {
        this.arrInlineFloat32T0x30.push(this._io.readF4be());
      }
      this.farDistance0x44 = (this._io.readF4be()) as any
      this.float32T0x48 = (this._io.readF4be()) as any
      this.float32T0x4c = (this._io.readF4be()) as any
      this.float32T0x50 = (this._io.readF4be()) as any
      this.float32T0x54 = (this._io.readF4be()) as any
      this.float32T0x58 = (this._io.readF4be()) as any
      this.nearDistance0x5c = (this._io.readF4be()) as any
      this.power0x60 = (this._io.readF4be()) as any
      this.float32T0x64 = (this._io.readF4be()) as any
      this.arrayCountFor0x30 = (this._io.readU2be()) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (108) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (790547232) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    colour0x10: GenericGenObject.RwMathVpuVector4;
    gameChangerId0x20: number;
    float32T0x24: number;
    float32T0x28: number;
    float32T0x2c: number;
    arrInlineFloat32T0x30: Array<number>;
    farDistance0x44: number;
    float32T0x48: number;
    float32T0x4c: number;
    float32T0x50: number;
    float32T0x54: number;
    float32T0x58: number;
    nearDistance0x5c: number;
    power0x60: number;
    float32T0x64: number;
    arrayCountFor0x30: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class T0006Cc77 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenericGenObject.Atype,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
    }

  }
}

export namespace GenericGenObject {
  export class GenesysGenEnvironmentKeyframe {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.cgsResourceHandle0xc = (this._io.readBytes(8)) as any
      this.colourCube0x14 = (this._io.readBytes(8)) as any
      this.gameChangerId0x1c = (this._io.readU4be()) as any
      this.unkEnum0x20 = (this._io.readU4be()) as any
      this.unkEnum0x24 = (this._io.readU4be()) as any
      this.unkEnum0x28 = (this._io.readU4be()) as any
      this.unkEnum0x2c = (this._io.readU4be()) as any
      this.unkEnum0x30 = (this._io.readU4be()) as any
      this.unkEnum0x34 = (this._io.readU4be()) as any
      this.unkEnum0x38 = (this._io.readU4be()) as any
      this.unkEnum0x3c = (this._io.readU4be()) as any
      this.unkEnum0x40 = (this._io.readU4be()) as any
    }

    private _inst000027Dd190x40: number | undefined;
    get inst000027Dd190x40(): number | undefined {
      if (typeof this._inst000027Dd190x40 !== 'undefined')
        return this._inst000027Dd190x40;
      if ((this.unkEnum0x40 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.unkEnum0x40 as any));
        this._inst000027Dd190x40 = (this._io.readU4be()) as any
        this._io.seek(_pos);
      }
      return this._inst000027Dd190x40;
    }

    private _inst000027Dd160x3c: number | undefined;
    get inst000027Dd160x3c(): number | undefined {
      if (typeof this._inst000027Dd160x3c !== 'undefined')
        return this._inst000027Dd160x3c;
      if ((this.unkEnum0x3c as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.unkEnum0x3c as any));
        this._inst000027Dd160x3c = (this._io.readU4be()) as any
        this._io.seek(_pos);
      }
      return this._inst000027Dd160x3c;
    }

    private _inst000027Dd130x38: number | undefined;
    get inst000027Dd130x38(): number | undefined {
      if (typeof this._inst000027Dd130x38 !== 'undefined')
        return this._inst000027Dd130x38;
      if ((this.unkEnum0x38 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.unkEnum0x38 as any));
        this._inst000027Dd130x38 = (this._io.readU4be()) as any
        this._io.seek(_pos);
      }
      return this._inst000027Dd130x38;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (68) as any
      return this._size;
    }

    private _inst000027Dd110x30: number | undefined;
    get inst000027Dd110x30(): number | undefined {
      if (typeof this._inst000027Dd110x30 !== 'undefined')
        return this._inst000027Dd110x30;
      if ((this.unkEnum0x30 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.unkEnum0x30 as any));
        this._inst000027Dd110x30 = (this._io.readU4be()) as any
        this._io.seek(_pos);
      }
      return this._inst000027Dd110x30;
    }

    private _inst000027Dd140x24: number | undefined;
    get inst000027Dd140x24(): number | undefined {
      if (typeof this._inst000027Dd140x24 !== 'undefined')
        return this._inst000027Dd140x24;
      if ((this.unkEnum0x24 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.unkEnum0x24 as any));
        this._inst000027Dd140x24 = (this._io.readU4be()) as any
        this._io.seek(_pos);
      }
      return this._inst000027Dd140x24;
    }

    private _inst000027Dd170x34: number | undefined;
    get inst000027Dd170x34(): number | undefined {
      if (typeof this._inst000027Dd170x34 !== 'undefined')
        return this._inst000027Dd170x34;
      if ((this.unkEnum0x34 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.unkEnum0x34 as any));
        this._inst000027Dd170x34 = (this._io.readU4be()) as any
        this._io.seek(_pos);
      }
      return this._inst000027Dd170x34;
    }

    private _inst000027Dd150x20: number | undefined;
    get inst000027Dd150x20(): number | undefined {
      if (typeof this._inst000027Dd150x20 !== 'undefined')
        return this._inst000027Dd150x20;
      if ((this.unkEnum0x20 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.unkEnum0x20 as any));
        this._inst000027Dd150x20 = (this._io.readU4be()) as any
        this._io.seek(_pos);
      }
      return this._inst000027Dd150x20;
    }

    private _inst000027Dd120x28: number | undefined;
    get inst000027Dd120x28(): number | undefined {
      if (typeof this._inst000027Dd120x28 !== 'undefined')
        return this._inst000027Dd120x28;
      if ((this.unkEnum0x28 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.unkEnum0x28 as any));
        this._inst000027Dd120x28 = (this._io.readU4be()) as any
        this._io.seek(_pos);
      }
      return this._inst000027Dd120x28;
    }

    private _inst000027Dd180x2c: number | undefined;
    get inst000027Dd180x2c(): number | undefined {
      if (typeof this._inst000027Dd180x2c !== 'undefined')
        return this._inst000027Dd180x2c;
      if ((this.unkEnum0x2c as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.unkEnum0x2c as any));
        this._inst000027Dd180x2c = (this._io.readU4be()) as any
        this._io.seek(_pos);
      }
      return this._inst000027Dd180x2c;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2353481207) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    cgsResourceHandle0xc: Uint8Array;
    colourCube0x14: Uint8Array;
    gameChangerId0x1c: number;

    /**
     * enum; 00_00_27_dd_1_5
     */
    unkEnum0x20: number;

    /**
     * enum; 00_00_27_dd_1_4
     */
    unkEnum0x24: number;

    /**
     * enum; 00_00_27_dd_1_2
     */
    unkEnum0x28: number;

    /**
     * enum; 00_00_27_dd_1_8
     */
    unkEnum0x2c: number;

    /**
     * enum; 00_00_27_dd_1_1
     */
    unkEnum0x30: number;

    /**
     * enum; 00_00_27_dd_1_7
     */
    unkEnum0x34: number;

    /**
     * enum; 00_00_27_dd_1_3
     */
    unkEnum0x38: number;

    /**
     * enum; 00_00_27_dd_1_6
     */
    unkEnum0x3c: number;

    /**
     * enum; 00_00_27_dd_1_9
     */
    unkEnum0x40: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenGameUnlockMilestone {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.cgsCoreUniqueId0x10 = (this._io.readU4be()) as any
      this.int32T0x14 = (this._io.readS4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (24) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (1216293293) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    cgsCoreUniqueId0x10: number;
    int32T0x14: number;
  }
}

export namespace GenericGenObject {
  export class GenesysGenWcsequenceBehaviour {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenBehaviour(this._io, this, this._root)) as any
      this.sequence0x1c = (this._io.readBytes(8)) as any
      this.bool8T0x24 = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(3)) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (40) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3428371066) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenBehaviour;
    sequence0x1c: Uint8Array;
    bool8T0x24: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenGameplayMilestone {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
      this.gameChangerId0xc = (this._io.readU4be()) as any
      this.message0x10 = (this._io.readU4be()) as any
      this.ptrArrEntries0x14 = (this._io.readU4be()) as any
      this.type0x18 = (this._io.readU2be()) as any
      this.arrayCountFor0x14 = (this._io.readU2be()) as any
      this.bool8T0x1c = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(3)) as any
    }

    private _instEntries0x14: Array<number | undefined> | undefined;
    get instEntries0x14(): Array<number | undefined> | undefined {
      if (typeof this._instEntries0x14 !== 'undefined')
        return this._instEntries0x14;
      if ((this.ptrArrEntries0x14 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.ptrArrEntries0x14 as any));
        this._instEntries0x14 = [];
        for (let i = 0; i < (this.arrayCountFor0x14 as any); i++) {
          this._instEntries0x14.push(this._io.readU4be());
        }
        this._io.seek(_pos);
      }
      return this._instEntries0x14;
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (32) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (2209408025) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenObj;
    gameChangerId0xc: number;
    message0x10: number;

    /**
     * enum; 00_00_32_cf_1
     */
    ptrArrEntries0x14: number;

    /**
     * enum; 00_00_2f_d0_1
     */
    type0x18: number;

    /**
     * "EntriesCount"
     */
    arrayCountFor0x14: number;
    bool8T0x1c: number;
    padding: Uint8Array;
  }
}

export namespace GenericGenObject {
  export class GenesysGenSmokeScreenWeapon {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenericGenObject,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenericGenObject.GenesysGenWeapon(this._io, this, this._root)) as any
      this.float32T0xb0 = (this._io.readF4be()) as any
      this.float32T0xb4 = (this._io.readF4be()) as any
      this.float32T0xb8 = (this._io.readF4be()) as any
      this.float32T0xbc = (this._io.readF4be()) as any
      this.float32T0xc0 = (this._io.readF4be()) as any
      this.float32T0xc4 = (this._io.readF4be()) as any
      this.float32T0xc8 = (this._io.readF4be()) as any
      this.float32T0xcc = (this._io.readF4be()) as any
      this.float32T0xd0 = (this._io.readF4be()) as any
      this.float32T0xd4 = (this._io.readF4be()) as any
      this.float32T0xd8 = (this._io.readF4be()) as any
    }

    private _size: number;
    get size(): number {
      if (typeof this._size !== 'undefined')
        return this._size;
      this._size = (220) as any
      return this._size;
    }

    private _muVersionHash: number;
    get muVersionHash(): number {
      if (typeof this._muVersionHash !== 'undefined')
        return this._muVersionHash;
      this._muVersionHash = (3302600098) as any
      return this._muVersionHash;
    }

    baseObject: GenericGenObject.GenesysGenWeapon;
    float32T0xb0: number;
    float32T0xb4: number;
    float32T0xb8: number;
    float32T0xbc: number;
    float32T0xc0: number;
    float32T0xc4: number;
    float32T0xc8: number;
    float32T0xcc: number;
    float32T0xd0: number;
    float32T0xd4: number;
    float32T0xd8: number;
  }
}

export namespace GenericGenObject {
  export class Atype {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: GenericGenObject.Ptr | undefined,
      readonly _root: GenericGenObject | undefined,
      dtype: string,
    ) {
      this.dtype = dtype;

      this._read();
    }

    _read() {
      switch ((this.dtype as any)) {
        case "genesys__gen__wcpath_animation_behaviour__animation_path": {
          this.data = (new GenericGenObject.GenesysGenWcpathAnimationBehaviourAnimationPath(this._io, this, this._root)) as any
          break;
        }
        case "string_base": {
          this.data = (new GenericGenObject.StringBase(this._io, this, this._root)) as any
          break;
        }
        case "t_70__f4__bb__e0": {
          this.data = (new GenericGenObject.T70F4BbE0(this._io, this, this._root)) as any
          break;
        }
        case "s4": {
          this.data = (this._io.readS4be()) as any
          break;
        }
        case "t_00_06__cc_72": {
          this.data = (new GenericGenObject.T0006Cc72(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__searchlight_behaviour": {
          this.data = (new GenericGenObject.GenesysGenSearchlightBehaviour(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__uilayout_instance_params": {
          this.data = (new GenericGenObject.GenesysGenUilayoutInstanceParams(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__aiplayer_type": {
          this.data = (new GenericGenObject.GenesysGenAiplayerType(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__uielement__scrollable_label": {
          this.data = (new GenericGenObject.GenesysGenUielementScrollableLabel(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__post_fxstate__value_modifier": {
          this.data = (new GenericGenObject.GenesysGenPostFxstateValueModifier(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__aiplayer_instance": {
          this.data = (new GenericGenObject.GenesysGenAiplayerInstance(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__event_location": {
          this.data = (new GenericGenObject.GenesysGenEventLocation(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__environment_keyframe__vfx": {
          this.data = (new GenericGenObject.GenesysGenEnvironmentKeyframeVfx(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__uicamera": {
          this.data = (new GenericGenObject.GenesysGenUicamera(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__physical_definition__rigid_body": {
          this.data = (new GenericGenObject.GenesysGenPhysicalDefinitionRigidBody(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__environment_timeline__timeline_keyframe": {
          this.data = (new GenericGenObject.GenesysGenEnvironmentTimelineTimelineKeyframe(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__arc_light_cone_upgrade": {
          this.data = (new GenericGenObject.GenesysGenArcLightConeUpgrade(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__dust_storm_minimap_upgrade": {
          this.data = (new GenericGenObject.GenesysGenDustStormMinimapUpgrade(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__uielement__mask": {
          this.data = (new GenericGenObject.GenesysGenUielementMask(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__perk_level": {
          this.data = (new GenericGenObject.GenesysGenPerkLevel(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__roadblock_instance": {
          this.data = (new GenericGenObject.GenesysGenRoadblockInstance(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__entitlement": {
          this.data = (new GenericGenObject.GenesysGenEntitlement(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__scoring_action": {
          this.data = (new GenericGenObject.GenesysGenScoringAction(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__uielement_base__effect_constant": {
          this.data = (new GenericGenObject.GenesysGenUielementBaseEffectConstant(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__animation_sequence_item": {
          this.data = (new GenericGenObject.GenesysGenAnimationSequenceItem(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__spike_strip_body_blow_upgrade": {
          this.data = (new GenericGenObject.GenesysGenSpikeStripBodyBlowUpgrade(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__environment_keyframe__camera": {
          this.data = (new GenericGenObject.GenesysGenEnvironmentKeyframeCamera(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__weapon_list": {
          this.data = (new GenericGenObject.GenesysGenWeaponList(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__post_fx_keyframe__general": {
          this.data = (new GenericGenObject.GenesysGenPostFxKeyframeGeneral(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__light__cone": {
          this.data = (new GenericGenObject.GenesysGenLightCone(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__camera_gameplay_shake_effect__translation__axis_params": {
          this.data = (new GenericGenObject.GenesysGenCameraGameplayShakeEffectTranslationAxisParams(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__physical_definition": {
          this.data = (new GenericGenObject.GenesysGenPhysicalDefinition(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__environment_keyframe__sky": {
          this.data = (new GenericGenObject.GenesysGenEnvironmentKeyframeSky(this._io, this, this._root)) as any
          break;
        }
        case "genesys__object": {
          this.data = (new GenericGenObject.GenesysObject(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__upgrade_package": {
          this.data = (new GenericGenObject.GenesysGenUpgradePackage(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__custom_chevron": {
          this.data = (new GenericGenObject.GenesysGenCustomChevron(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__sequence_item": {
          this.data = (new GenericGenObject.GenesysGenSequenceItem(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__mixer_channel__priority": {
          this.data = (new GenericGenObject.GenesysGenMixerChannelPriority(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__wcvfx_behaviour__lights": {
          this.data = (new GenericGenObject.GenesysGenWcvfxBehaviourLights(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__physical_explosion__race_car_in_air_explosion": {
          this.data = (new GenericGenObject.GenesysGenPhysicalExplosionRaceCarInAirExplosion(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__camera_gameplay_shake_effect__translation": {
          this.data = (new GenericGenObject.GenesysGenCameraGameplayShakeEffectTranslation(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__offline_event": {
          this.data = (new GenericGenObject.GenesysGenOfflineEvent(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__corona": {
          this.data = (new GenericGenObject.GenesysGenCorona(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__event_arena": {
          this.data = (new GenericGenObject.GenesysGenEventArena(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__uitechnique": {
          this.data = (new GenericGenObject.GenesysGenUitechnique(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__post_fx_keyframe__depth_of__field": {
          this.data = (new GenericGenObject.GenesysGenPostFxKeyframeDepthOfField(this._io, this, this._root)) as any
          break;
        }
        case "t_00_03__f8_50": {
          this.data = (new GenericGenObject.T0003F850(this._io, this, this._root)) as any
          break;
        }
        case "t_0c_96_6a_95": {
          this.data = (new GenericGenObject.T0c966a95(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__corona__beam": {
          this.data = (new GenericGenObject.GenesysGenCoronaBeam(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__rollout": {
          this.data = (new GenericGenObject.GenesysGenRollout(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__uielement_base__behaviour": {
          this.data = (new GenericGenObject.GenesysGenUielementBaseBehaviour(this._io, this, this._root)) as any
          break;
        }
        case "t_00_00_31__ca": {
          this.data = (new GenericGenObject.T000031Ca(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__offline_event__custom_chevrons": {
          this.data = (new GenericGenObject.GenesysGenOfflineEventCustomChevrons(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__flash_bang_weapon": {
          this.data = (new GenericGenObject.GenesysGenFlashBangWeapon(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__online_event": {
          this.data = (new GenericGenObject.GenesysGenOnlineEvent(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__make_physical_behaviour": {
          this.data = (new GenericGenObject.GenesysGenMakePhysicalBehaviour(this._io, this, this._root)) as any
          break;
        }
        case "cgs_core__unique_id": {
          this.data = (new GenericGenObject.CgsCoreUniqueId(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__corona__env_map_glow": {
          this.data = (new GenericGenObject.GenesysGenCoronaEnvMapGlow(this._io, this, this._root)) as any
          break;
        }
        case "bool8_t": {
          this.data = (new GenericGenObject.Bool8T(this._io, this, this._root)) as any
          break;
        }
        case "ff__ff__ff__f8": {
          this.data = (new GenericGenObject.FfFfFfF8(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__post_fx_keyframe": {
          this.data = (new GenericGenObject.GenesysGenPostFxKeyframe(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__nucleus_grant_mappings_list__mapping": {
          this.data = (new GenericGenObject.GenesysGenNucleusGrantMappingsListMapping(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__grenade_weapon": {
          this.data = (new GenericGenObject.GenesysGenGrenadeWeapon(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__vfx_spot_effect_sequence_item": {
          this.data = (new GenericGenObject.GenesysGenVfxSpotEffectSequenceItem(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__wcpath_animation_behaviour": {
          this.data = (new GenericGenObject.GenesysGenWcpathAnimationBehaviour(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__environment_keyframe__heat_haze": {
          this.data = (new GenericGenObject.GenesysGenEnvironmentKeyframeHeatHaze(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__gameplay_trigger": {
          this.data = (new GenericGenObject.GenesysGenGameplayTrigger(this._io, this, this._root)) as any
          break;
        }
        case "s1": {
          this.data = (this._io.readS1()) as any
          break;
        }
        case "genesys__gen__weapon_upgrade": {
          this.data = (new GenericGenObject.GenesysGenWeaponUpgrade(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__uielement__movie_player__dimensions": {
          this.data = (new GenericGenObject.GenesysGenUielementMoviePlayerDimensions(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__post_fxsequence_item": {
          this.data = (new GenericGenObject.GenesysGenPostFxsequenceItem(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__nitrous_burning_game_rule": {
          this.data = (new GenericGenObject.GenesysGenNitrousBurningGameRule(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__impact_damage_game_rule": {
          this.data = (new GenericGenObject.GenesysGenImpactDamageGameRule(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__camera_gameplay_shake_effect__rotation__axis_params": {
          this.data = (new GenericGenObject.GenesysGenCameraGameplayShakeEffectRotationAxisParams(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__extra_ammo_weapon_upgrade": {
          this.data = (new GenericGenObject.GenesysGenExtraAmmoWeaponUpgrade(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__game_unlock": {
          this.data = (new GenericGenObject.GenesysGenGameUnlock(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__heat_level__cop_type": {
          this.data = (new GenericGenObject.GenesysGenHeatLevelCopType(this._io, this, this._root)) as any
          break;
        }
        case "float32_t": {
          this.data = (new GenericGenObject.Float32T(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__uielement__scrollable_label__string": {
          this.data = (new GenericGenObject.GenesysGenUielementScrollableLabelString(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__nucleus_entitlement_tag": {
          this.data = (new GenericGenObject.GenesysGenNucleusEntitlementTag(this._io, this, this._root)) as any
          break;
        }
        case "u4": {
          this.data = (this._io.readU4be()) as any
          break;
        }
        case "genesys__gen__uimaterial": {
          this.data = (new GenericGenObject.GenesysGenUimaterial(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__road_block_definition": {
          this.data = (new GenericGenObject.GenesysGenRoadBlockDefinition(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__event_arena_data": {
          this.data = (new GenericGenObject.GenesysGenEventArenaData(this._io, this, this._root)) as any
          break;
        }
        case "t_34_26_5a_75": {
          this.data = (new GenericGenObject.T34265a75(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__thank_you_screen_item": {
          this.data = (new GenericGenObject.GenesysGenThankYouScreenItem(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__uielement__mini_map": {
          this.data = (new GenericGenObject.GenesysGenUielementMiniMap(this._io, this, this._root)) as any
          break;
        }
        case "t_00_03__f6_83": {
          this.data = (new GenericGenObject.T0003F683(this._io, this, this._root)) as any
          break;
        }
        case "gen_obj": {
          this.data = (new GenericGenObject.GenObj(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__corona__glow": {
          this.data = (new GenericGenObject.GenesysGenCoronaGlow(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__light__base__flash_pattern": {
          this.data = (new GenericGenObject.GenesysGenLightBaseFlashPattern(this._io, this, this._root)) as any
          break;
        }
        case "t_40_99__f3__ac": {
          this.data = (new GenericGenObject.T4099F3Ac(this._io, this, this._root)) as any
          break;
        }
        case "u2": {
          this.data = (this._io.readU2be()) as any
          break;
        }
        case "cgs_resource__handle": {
          this.data = (new GenericGenObject.CgsResourceHandle(this._io, this, this._root)) as any
          break;
        }
        case "t_00_07_57_09": {
          this.data = (new GenericGenObject.T00075709(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__score_view_model": {
          this.data = (new GenericGenObject.GenesysGenScoreViewModel(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__environment_keyframe__weather": {
          this.data = (new GenericGenObject.GenesysGenEnvironmentKeyframeWeather(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__teflon_slick_weapon": {
          this.data = (new GenericGenObject.GenesysGenTeflonSlickWeapon(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__performance_upgrade_package": {
          this.data = (new GenericGenObject.GenesysGenPerformanceUpgradePackage(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__text_style__text_style_locale": {
          this.data = (new GenericGenObject.GenesysGenTextStyleTextStyleLocale(this._io, this, this._root)) as any
          break;
        }
        case "t_00_00_30_1d": {
          this.data = (new GenericGenObject.T0000301d(this._io, this, this._root)) as any
          break;
        }
        case "rw_math_vpu__matrix44affine": {
          this.data = (new GenericGenObject.RwMathVpuMatrix44affine(this._io, this, this._root)) as any
          break;
        }
        case "t_5b_33_21__f5": {
          this.data = (new GenericGenObject.T5b3321F5(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__mixing_group": {
          this.data = (new GenericGenObject.GenesysGenMixingGroup(this._io, this, this._root)) as any
          break;
        }
        case "int16_t": {
          this.data = (new GenericGenObject.Int16T(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__helicopter_weapon": {
          this.data = (new GenericGenObject.GenesysGenHelicopterWeapon(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__wcvfx_behaviour__spot_effects": {
          this.data = (new GenericGenObject.GenesysGenWcvfxBehaviourSpotEffects(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__text_style": {
          this.data = (new GenericGenObject.GenesysGenTextStyle(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__perk": {
          this.data = (new GenericGenObject.GenesysGenPerk(this._io, this, this._root)) as any
          break;
        }
        case "s2": {
          this.data = (this._io.readS2be()) as any
          break;
        }
        case "genesys__gen__wave_sequence_item__fade": {
          this.data = (new GenericGenObject.GenesysGenWaveSequenceItemFade(this._io, this, this._root)) as any
          break;
        }
        case "t_00_09_37__a3": {
          this.data = (new GenericGenObject.T000937A3(this._io, this, this._root)) as any
          break;
        }
        case "t_00_00_30_35": {
          this.data = (new GenericGenObject.T00003035(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__game_unlock__milestone": {
          this.data = (new GenericGenObject.GenesysGenGameUnlockMilestone(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__wcsequence_behaviour": {
          this.data = (new GenericGenObject.GenesysGenWcsequenceBehaviour(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__rollout__weapon_data": {
          this.data = (new GenericGenObject.GenesysGenRolloutWeaponData(this._io, this, this._root)) as any
          break;
        }
        case "t_00_04_5f__b1": {
          this.data = (new GenericGenObject.T00045fB1(this._io, this, this._root)) as any
          break;
        }
        case "t_00_00_31__b6": {
          this.data = (new GenericGenObject.T000031B6(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__jump_timeline_controller": {
          this.data = (new GenericGenObject.GenesysGenJumpTimelineController(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__physical_definition__rigid_body__sphere_volume": {
          this.data = (new GenericGenObject.GenesysGenPhysicalDefinitionRigidBodySphereVolume(this._io, this, this._root)) as any
          break;
        }
        case "t_06__a9_64__cd": {
          this.data = (new GenericGenObject.T06A964Cd(this._io, this, this._root)) as any
          break;
        }
        case "t_00_05__f7_0e": {
          this.data = (new GenericGenObject.T0005F70e(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__gameplay_trigger__input": {
          this.data = (new GenericGenObject.GenesysGenGameplayTriggerInput(this._io, this, this._root)) as any
          break;
        }
        case "t_00_00_2f__d0": {
          this.data = (new GenericGenObject.T00002fD0(this._io, this, this._root)) as any
          break;
        }
        case "strz": {
          this.data = (KaitaiStream.bytesToStr(this._io.readBytesTerm(0, false, true, true), "ascii")) as any
          break;
        }
        case "genesys__gen__physical_definition__rigid_body__convex_hull_volume": {
          this.data = (new GenericGenObject.GenesysGenPhysicalDefinitionRigidBodyConvexHullVolume(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__fast_launch_weapon_upgrade": {
          this.data = (new GenericGenObject.GenesysGenFastLaunchWeaponUpgrade(this._io, this, this._root)) as any
          break;
        }
        case "genesys_obj_collection": {
          this.data = (new GenericGenObject.GenesysObjCollection(this._io, this, this._root)) as any
          break;
        }
        case "t_00_00_30_27": {
          this.data = (new GenericGenObject.T00003027(this._io, this, this._root)) as any
          break;
        }
        case "t_05_89__a9_77": {
          this.data = (new GenericGenObject.T0589A977(this._io, this, this._root)) as any
          break;
        }
        case "t_00_06__cc_77": {
          this.data = (new GenericGenObject.T0006Cc77(this._io, this, this._root)) as any
          break;
        }
        case "c9_7e__aa__da": {
          this.data = (new GenericGenObject.C97eAaDa(this._io, this, this._root)) as any
          break;
        }
        case "t_8e_7d_5f_21": {
          this.data = (new GenericGenObject.T8e7d5f21(this._io, this, this._root)) as any
          break;
        }
        case "t_00_04_63_4a": {
          this.data = (new GenericGenObject.T0004634a(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__weapon_recharge_data": {
          this.data = (new GenericGenObject.GenesysGenWeaponRechargeData(this._io, this, this._root)) as any
          break;
        }
        case "t_00_06__fa_70": {
          this.data = (new GenericGenObject.T0006Fa70(this._io, this, this._root)) as any
          break;
        }
        case "t_00_00_2f__f0": {
          this.data = (new GenericGenObject.T00002fF0(this._io, this, this._root)) as any
          break;
        }
        case "t_00_00_30_38": {
          this.data = (new GenericGenObject.T00003038(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__wcvfx_behaviour__coronas": {
          this.data = (new GenericGenObject.GenesysGenWcvfxBehaviourCoronas(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__physical_definition__rigid_body__cylinder_volume": {
          this.data = (new GenericGenObject.GenesysGenPhysicalDefinitionRigidBodyCylinderVolume(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__nitrous_earning_game_rule": {
          this.data = (new GenericGenObject.GenesysGenNitrousEarningGameRule(this._io, this, this._root)) as any
          break;
        }
        case "rw_math_vpu__vector3": {
          this.data = (new GenericGenObject.RwMathVpuVector3(this._io, this, this._root)) as any
          break;
        }
        case "rw__rgba": {
          this.data = (new GenericGenObject.RwRgba(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__physical_explosion__non_race_car_explosion": {
          this.data = (new GenericGenObject.GenesysGenPhysicalExplosionNonRaceCarExplosion(this._io, this, this._root)) as any
          break;
        }
        case "t_95_95_0d_30": {
          this.data = (new GenericGenObject.T95950d30(this._io, this, this._root)) as any
          break;
        }
        case "rw_math_vpu__vector2": {
          this.data = (new GenericGenObject.RwMathVpuVector2(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__silent_launch_weapon_upgrade": {
          this.data = (new GenericGenObject.GenesysGenSilentLaunchWeaponUpgrade(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__physical_explosion__gameplay_explosion": {
          this.data = (new GenericGenObject.GenesysGenPhysicalExplosionGameplayExplosion(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__uielement_base": {
          this.data = (new GenericGenObject.GenesysGenUielementBase(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__device_grant_upgrade_package": {
          this.data = (new GenericGenObject.GenesysGenDeviceGrantUpgradePackage(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__environment_keyframe__fog": {
          this.data = (new GenericGenObject.GenesysGenEnvironmentKeyframeFog(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__event": {
          this.data = (new GenericGenObject.GenesysGenEvent(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__sequence_timeline_controller": {
          this.data = (new GenericGenObject.GenesysGenSequenceTimelineController(this._io, this, this._root)) as any
          break;
        }
        case "a7_6d_0e_28": {
          this.data = (new GenericGenObject.A76d0e28(this._io, this, this._root)) as any
          break;
        }
        case "f4": {
          this.data = (this._io.readF4be()) as any
          break;
        }
        case "u1": {
          this.data = (this._io.readU1()) as any
          break;
        }
        case "genesys__gen__uielement__prototype_shape": {
          this.data = (new GenericGenObject.GenesysGenUielementPrototypeShape(this._io, this, this._root)) as any
          break;
        }
        case "uint16_t": {
          this.data = (new GenericGenObject.Uint16T(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__weapon": {
          this.data = (new GenericGenObject.GenesysGenWeapon(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__uielement__prototype_image__tint_properties": {
          this.data = (new GenericGenObject.GenesysGenUielementPrototypeImageTintProperties(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__camera_gameplay_shake_effect__rotation": {
          this.data = (new GenericGenObject.GenesysGenCameraGameplayShakeEffectRotation(this._io, this, this._root)) as any
          break;
        }
        case "t_00_00_31__c4": {
          this.data = (new GenericGenObject.T000031C4(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__post_fx_keyframe__vignette": {
          this.data = (new GenericGenObject.GenesysGenPostFxKeyframeVignette(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__game_mode__score_override": {
          this.data = (new GenericGenObject.GenesysGenGameModeScoreOverride(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__wave_sequence_item": {
          this.data = (new GenericGenObject.GenesysGenWaveSequenceItem(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__score_view_model__score_data": {
          this.data = (new GenericGenObject.GenesysGenScoreViewModelScoreData(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__light__point": {
          this.data = (new GenericGenObject.GenesysGenLightPoint(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__road_block_layer__item": {
          this.data = (new GenericGenObject.GenesysGenRoadBlockLayerItem(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__spike_strip_blowout_upgrade": {
          this.data = (new GenericGenObject.GenesysGenSpikeStripBlowoutUpgrade(this._io, this, this._root)) as any
          break;
        }
        case "t_00_00_30_3d": {
          this.data = (new GenericGenObject.T0000303d(this._io, this, this._root)) as any
          break;
        }
        case "t_00_09_37_93": {
          this.data = (new GenericGenObject.T00093793(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__physical_definition__rigid_body__capsule_volume": {
          this.data = (new GenericGenObject.GenesysGenPhysicalDefinitionRigidBodyCapsuleVolume(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__store_item": {
          this.data = (new GenericGenObject.GenesysGenStoreItem(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__uicolour": {
          this.data = (new GenericGenObject.GenesysGenUicolour(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__add_behaviour_sequence_item": {
          this.data = (new GenericGenObject.GenesysGenAddBehaviourSequenceItem(this._io, this, this._root)) as any
          break;
        }
        case "t_35__a6_06_1e": {
          this.data = (new GenericGenObject.T35A6061e(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__vision_mode": {
          this.data = (new GenericGenObject.GenesysGenVisionMode(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__camera_gameplay_shake_effect": {
          this.data = (new GenericGenObject.GenesysGenCameraGameplayShakeEffect(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__apply_vehicle_kick_sequence_item": {
          this.data = (new GenericGenObject.GenesysGenApplyVehicleKickSequenceItem(this._io, this, this._root)) as any
          break;
        }
        case "t_00_06__fa_71": {
          this.data = (new GenericGenObject.T0006Fa71(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__spike_strip_weapon": {
          this.data = (new GenericGenObject.GenesysGenSpikeStripWeapon(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__mixer_channel": {
          this.data = (new GenericGenObject.GenesysGenMixerChannel(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__gameplay_trigger__output__sequence_output": {
          this.data = (new GenericGenObject.GenesysGenGameplayTriggerOutputSequenceOutput(this._io, this, this._root)) as any
          break;
        }
        case "t_00_05__f6_43": {
          this.data = (new GenericGenObject.T0005F643(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__camera_shake_sequence_item": {
          this.data = (new GenericGenObject.GenesysGenCameraShakeSequenceItem(this._io, this, this._root)) as any
          break;
        }
        case "da__dc_9b_17": {
          this.data = (new GenericGenObject.DaDc9b17(this._io, this, this._root)) as any
          break;
        }
        case "t_00_04_5e__f1": {
          this.data = (new GenericGenObject.T00045eF1(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__heat_level": {
          this.data = (new GenericGenObject.GenesysGenHeatLevel(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__physics_sequence_item__physics_double_value": {
          this.data = (new GenericGenObject.GenesysGenPhysicsSequenceItemPhysicsDoubleValue(this._io, this, this._root)) as any
          break;
        }
        case "d0_00_70_01": {
          this.data = (new GenericGenObject.D0007001(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__uielement_base__rendering_data": {
          this.data = (new GenericGenObject.GenesysGenUielementBaseRenderingData(this._io, this, this._root)) as any
          break;
        }
        case "t_00_06__cc_2f": {
          this.data = (new GenericGenObject.T0006Cc2f(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__environment_keyframe__light_rig": {
          this.data = (new GenericGenObject.GenesysGenEnvironmentKeyframeLightRig(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__physical_explosion": {
          this.data = (new GenericGenObject.GenesysGenPhysicalExplosion(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__uielement__main_map": {
          this.data = (new GenericGenObject.GenesysGenUielementMainMap(this._io, this, this._root)) as any
          break;
        }
        case "t_00_03__f3__c4": {
          this.data = (new GenericGenObject.T0003F3C4(this._io, this, this._root)) as any
          break;
        }
        case "int32_t": {
          this.data = (new GenericGenObject.Int32T(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__game_unlock_list": {
          this.data = (new GenericGenObject.GenesysGenGameUnlockList(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__uilayout": {
          this.data = (new GenericGenObject.GenesysGenUilayout(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__gameplay_milestone__entry": {
          this.data = (new GenericGenObject.GenesysGenGameplayMilestoneEntry(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__light__base": {
          this.data = (new GenericGenObject.GenesysGenLightBase(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__mine_weapon": {
          this.data = (new GenericGenObject.GenesysGenMineWeapon(this._io, this, this._root)) as any
          break;
        }
        case "f7__ff__d1__f8": {
          this.data = (new GenericGenObject.F7FfD1F8(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__event_list": {
          this.data = (new GenericGenObject.GenesysGenEventList(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__uielement__prototype_scrolling_text__text_properties": {
          this.data = (new GenericGenObject.GenesysGenUielementPrototypeScrollingTextTextProperties(this._io, this, this._root)) as any
          break;
        }
        case "t_00_07__bc_8a": {
          this.data = (new GenericGenObject.T0007Bc8a(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__event_trigger_sequence_item": {
          this.data = (new GenericGenObject.GenesysGenEventTriggerSequenceItem(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__environment_timeline_sequence_item": {
          this.data = (new GenericGenObject.GenesysGenEnvironmentTimelineSequenceItem(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__nucleus_grant_mappings_list": {
          this.data = (new GenericGenObject.GenesysGenNucleusGrantMappingsList(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__thankyou_mapping": {
          this.data = (new GenericGenObject.GenesysGenThankyouMapping(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__sound_distance_falloff": {
          this.data = (new GenericGenObject.GenesysGenSoundDistanceFalloff(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__uielement__prototype_label": {
          this.data = (new GenericGenObject.GenesysGenUielementPrototypeLabel(this._io, this, this._root)) as any
          break;
        }
        case "char": {
          this.data = (new GenericGenObject.Char(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__store_pack_list": {
          this.data = (new GenericGenObject.GenesysGenStorePackList(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__game_rank": {
          this.data = (new GenericGenObject.GenesysGenGameRank(this._io, this, this._root)) as any
          break;
        }
        case "t_96__c1_53_69": {
          this.data = (new GenericGenObject.T96C15369(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__physical_explosion__race_car_on_ground_explosion": {
          this.data = (new GenericGenObject.GenesysGenPhysicalExplosionRaceCarOnGroundExplosion(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__snap_to_world_behaviour": {
          this.data = (new GenericGenObject.GenesysGenSnapToWorldBehaviour(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__store_pack": {
          this.data = (new GenericGenObject.GenesysGenStorePack(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__wcvfx_behaviour": {
          this.data = (new GenericGenObject.GenesysGenWcvfxBehaviour(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__post_fxstate__colour_cube_settings": {
          this.data = (new GenericGenObject.GenesysGenPostFxstateColourCubeSettings(this._io, this, this._root)) as any
          break;
        }
        case "t_00_00_31__d2": {
          this.data = (new GenericGenObject.T000031D2(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__uielement__prototype_image": {
          this.data = (new GenericGenObject.GenesysGenUielementPrototypeImage(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__game_pack": {
          this.data = (new GenericGenObject.GenesysGenGamePack(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__uielement__prototype_scrolling_text__string": {
          this.data = (new GenericGenObject.GenesysGenUielementPrototypeScrollingTextString(this._io, this, this._root)) as any
          break;
        }
        case "t_00_00_2f__c8": {
          this.data = (new GenericGenObject.T00002fC8(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__jammer_weapon": {
          this.data = (new GenericGenObject.GenesysGenJammerWeapon(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__set_vision_mode_type_sequence_item": {
          this.data = (new GenericGenObject.GenesysGenSetVisionModeTypeSequenceItem(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__environment_timeline": {
          this.data = (new GenericGenObject.GenesysGenEnvironmentTimeline(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__uielement__prototype_scrolling_text": {
          this.data = (new GenericGenObject.GenesysGenUielementPrototypeScrollingText(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__uielement__prototype_image__opacity": {
          this.data = (new GenericGenObject.GenesysGenUielementPrototypeImageOpacity(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__uielement__scrollable_label__text_properties": {
          this.data = (new GenericGenObject.GenesysGenUielementScrollableLabelTextProperties(this._io, this, this._root)) as any
          break;
        }
        case "t_00_05__f3_93": {
          this.data = (new GenericGenObject.T0005F393(this._io, this, this._root)) as any
          break;
        }
        case "t_00_03__f7_15": {
          this.data = (new GenericGenObject.T0003F715(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__speedbreaker_weapon": {
          this.data = (new GenericGenObject.GenesysGenSpeedbreakerWeapon(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__thermal_vision_mode": {
          this.data = (new GenericGenObject.GenesysGenThermalVisionMode(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__behaviour": {
          this.data = (new GenericGenObject.GenesysGenBehaviour(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__uilayout_instance_params__timeline_parameters": {
          this.data = (new GenericGenObject.GenesysGenUilayoutInstanceParamsTimelineParameters(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__uielement__prototype_label__text_properties": {
          this.data = (new GenericGenObject.GenesysGenUielementPrototypeLabelTextProperties(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__post_fxstate": {
          this.data = (new GenericGenObject.GenesysGenPostFxstate(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__game_mode": {
          this.data = (new GenericGenObject.GenesysGenGameMode(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__uielement_base__timeline__behaviour": {
          this.data = (new GenericGenObject.GenesysGenUielementBaseTimelineBehaviour(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__corona__flare": {
          this.data = (new GenericGenObject.GenesysGenCoronaFlare(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__gameplay_milestone": {
          this.data = (new GenericGenObject.GenesysGenGameplayMilestone(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__chevron": {
          this.data = (new GenericGenObject.GenesysGenChevron(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__sequence": {
          this.data = (new GenericGenObject.GenesysGenSequence(this._io, this, this._root)) as any
          break;
        }
        case "rw_math_vpu__vector4": {
          this.data = (new GenericGenObject.RwMathVpuVector4(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__uielement__element_stack__template": {
          this.data = (new GenericGenObject.GenesysGenUielementElementStackTemplate(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__uielement_base__timeline": {
          this.data = (new GenericGenObject.GenesysGenUielementBaseTimeline(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__environment_keyframe__mini__dof": {
          this.data = (new GenericGenObject.GenesysGenEnvironmentKeyframeMiniDof(this._io, this, this._root)) as any
          break;
        }
        case "t_00_03__f6__d5": {
          this.data = (new GenericGenObject.T0003F6D5(this._io, this, this._root)) as any
          break;
        }
        case "t_00_04_5f__ad": {
          this.data = (new GenericGenObject.T00045fAd(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__road_block_layer": {
          this.data = (new GenericGenObject.GenesysGenRoadBlockLayer(this._io, this, this._root)) as any
          break;
        }
        case "t_00_07_33__ee": {
          this.data = (new GenericGenObject.T000733Ee(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__uilayout_instance_params__transform_components": {
          this.data = (new GenericGenObject.GenesysGenUilayoutInstanceParamsTransformComponents(this._io, this, this._root)) as any
          break;
        }
        case "generic_gen_object": {
          this.data = (new GenericGenObject(this._io, this, null)) as any
          break;
        }
        case "genesys__gen__layout_sequence_item": {
          this.data = (new GenericGenObject.GenesysGenLayoutSequenceItem(this._io, this, this._root)) as any
          break;
        }
        case "d7__b2_21__da": {
          this.data = (new GenericGenObject.D7B221Da(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__physics_sequence_item": {
          this.data = (new GenericGenObject.GenesysGenPhysicsSequenceItem(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__nucleus_entitlement_tags": {
          this.data = (new GenericGenObject.GenesysGenNucleusEntitlementTags(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__wcplay_sound_behaviour__prop_surface_sound": {
          this.data = (new GenericGenObject.GenesysGenWcplaySoundBehaviourPropSurfaceSound(this._io, this, this._root)) as any
          break;
        }
        case "cgs_core__string_base": {
          this.data = (new GenericGenObject.CgsCoreStringBase(this._io, this, this._root)) as any
          break;
        }
        case "t_00_00_30_22": {
          this.data = (new GenericGenObject.T00003022(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__game_unlock__event": {
          this.data = (new GenericGenObject.GenesysGenGameUnlockEvent(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__uielement__prototype_label__string": {
          this.data = (new GenericGenObject.GenesysGenUielementPrototypeLabelString(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__gameplay_trigger__output": {
          this.data = (new GenericGenObject.GenesysGenGameplayTriggerOutput(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__uielement__element_stack": {
          this.data = (new GenericGenObject.GenesysGenUielementElementStack(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__bus_mixer_channel_sequence_item__bus_mixer_channel_double_value": {
          this.data = (new GenericGenObject.GenesysGenBusMixerChannelSequenceItemBusMixerChannelDoubleValue(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__physical_definition__rigid_body__box_volume": {
          this.data = (new GenericGenObject.GenesysGenPhysicalDefinitionRigidBodyBoxVolume(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__car_select_data": {
          this.data = (new GenericGenObject.GenesysGenCarSelectData(this._io, this, this._root)) as any
          break;
        }
        case "uint8_t": {
          this.data = (new GenericGenObject.Uint8T(this._io, this, this._root)) as any
          break;
        }
        case "t_00_00_2e__a1": {
          this.data = (new GenericGenObject.T00002eA1(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__smoke_screen_weapon": {
          this.data = (new GenericGenObject.GenesysGenSmokeScreenWeapon(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__hypox_particles_weapon_upgrade": {
          this.data = (new GenericGenObject.GenesysGenHypoxParticlesWeaponUpgrade(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__post_fx_keyframe__stereo_3d": {
          this.data = (new GenericGenObject.GenesysGenPostFxKeyframeStereo3d(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__car_select_data__sequences": {
          this.data = (new GenericGenObject.GenesysGenCarSelectDataSequences(this._io, this, this._root)) as any
          break;
        }
        case "t_00_06__fa_8a": {
          this.data = (new GenericGenObject.T0006Fa8a(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__hud_style_sequence_item": {
          this.data = (new GenericGenObject.GenesysGenHudStyleSequenceItem(this._io, this, this._root)) as any
          break;
        }
        case "t_00_05__ab_65": {
          this.data = (new GenericGenObject.T0005Ab65(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__wcplay_sound_behaviour": {
          this.data = (new GenericGenObject.GenesysGenWcplaySoundBehaviour(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__post_fx_keyframe__bloom": {
          this.data = (new GenericGenObject.GenesysGenPostFxKeyframeBloom(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__bus_mixer_channel_sequence_item": {
          this.data = (new GenericGenObject.GenesysGenBusMixerChannelSequenceItem(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__sequence_item__modulating_double_value": {
          this.data = (new GenericGenObject.GenesysGenSequenceItemModulatingDoubleValue(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__wchide_behaviour": {
          this.data = (new GenericGenObject.GenesysGenWchideBehaviour(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__uielement__movie_player": {
          this.data = (new GenericGenObject.GenesysGenUielementMoviePlayer(this._io, this, this._root)) as any
          break;
        }
        case "uint32_t": {
          this.data = (new GenericGenObject.Uint32T(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__environment_keyframe": {
          this.data = (new GenericGenObject.GenesysGenEnvironmentKeyframe(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__thermal_vision_mode_properties": {
          this.data = (new GenericGenObject.GenesysGenThermalVisionModeProperties(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__slow_mo_sequence_item": {
          this.data = (new GenericGenObject.GenesysGenSlowMoSequenceItem(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__impact_protection_game_rule": {
          this.data = (new GenericGenObject.GenesysGenImpactProtectionGameRule(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__flash_headlights_weapon": {
          this.data = (new GenericGenObject.GenesysGenFlashHeadlightsWeapon(this._io, this, this._root)) as any
          break;
        }
        case "t_00_00_31__ba": {
          this.data = (new GenericGenObject.T000031Ba(this._io, this, this._root)) as any
          break;
        }
        case "t_35__d6_2d_64": {
          this.data = (new GenericGenObject.T35D62d64(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__environment_keyframe__clouds": {
          this.data = (new GenericGenObject.GenesysGenEnvironmentKeyframeClouds(this._io, this, this._root)) as any
          break;
        }
        case "t_00_03__f6_5b": {
          this.data = (new GenericGenObject.T0003F65b(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__wcremove_world_entity_behaviour": {
          this.data = (new GenericGenObject.GenesysGenWcremoveWorldEntityBehaviour(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__game_rule": {
          this.data = (new GenericGenObject.GenesysGenGameRule(this._io, this, this._root)) as any
          break;
        }
        default: {
          this.data = (new GenericGenObject.Dummy(this._io, this, this._root)) as any
          break;
        }
      }
    }

    data: GenericGenObject.GenesysGenWcpathAnimationBehaviourAnimationPath | GenericGenObject.StringBase | GenericGenObject.T70F4BbE0 | number | GenericGenObject.T0006Cc72 | GenericGenObject.GenesysGenSearchlightBehaviour | GenericGenObject.GenesysGenUilayoutInstanceParams | GenericGenObject.GenesysGenAiplayerType | GenericGenObject.GenesysGenUielementScrollableLabel | GenericGenObject.GenesysGenPostFxstateValueModifier | GenericGenObject.GenesysGenAiplayerInstance | GenericGenObject.GenesysGenEventLocation | GenericGenObject.GenesysGenEnvironmentKeyframeVfx | GenericGenObject.GenesysGenUicamera | GenericGenObject.GenesysGenPhysicalDefinitionRigidBody | GenericGenObject.GenesysGenEnvironmentTimelineTimelineKeyframe | GenericGenObject.GenesysGenArcLightConeUpgrade | GenericGenObject.GenesysGenDustStormMinimapUpgrade | GenericGenObject.GenesysGenUielementMask | GenericGenObject.GenesysGenPerkLevel | GenericGenObject.GenesysGenRoadblockInstance | GenericGenObject.GenesysGenEntitlement | GenericGenObject.GenesysGenScoringAction | GenericGenObject.GenesysGenUielementBaseEffectConstant | GenericGenObject.GenesysGenAnimationSequenceItem | GenericGenObject.GenesysGenSpikeStripBodyBlowUpgrade | GenericGenObject.GenesysGenEnvironmentKeyframeCamera | GenericGenObject.GenesysGenWeaponList | GenericGenObject.GenesysGenPostFxKeyframeGeneral | GenericGenObject.GenesysGenLightCone | GenericGenObject.GenesysGenCameraGameplayShakeEffectTranslationAxisParams | GenericGenObject.GenesysGenPhysicalDefinition | GenericGenObject.GenesysGenEnvironmentKeyframeSky | GenericGenObject.GenesysObject | GenericGenObject.GenesysGenUpgradePackage | GenericGenObject.GenesysGenCustomChevron | GenericGenObject.GenesysGenSequenceItem | GenericGenObject.GenesysGenMixerChannelPriority | GenericGenObject.GenesysGenWcvfxBehaviourLights | GenericGenObject.GenesysGenPhysicalExplosionRaceCarInAirExplosion | GenericGenObject.GenesysGenCameraGameplayShakeEffectTranslation | GenericGenObject.GenesysGenOfflineEvent | GenericGenObject.GenesysGenCorona | GenericGenObject.GenesysGenEventArena | GenericGenObject.GenesysGenUitechnique | GenericGenObject.GenesysGenPostFxKeyframeDepthOfField | GenericGenObject.T0003F850 | GenericGenObject.T0c966a95 | GenericGenObject.GenesysGenCoronaBeam | GenericGenObject.GenesysGenRollout | GenericGenObject.GenesysGenUielementBaseBehaviour | GenericGenObject.T000031Ca | GenericGenObject.GenesysGenOfflineEventCustomChevrons | GenericGenObject.GenesysGenFlashBangWeapon | GenericGenObject.GenesysGenOnlineEvent | GenericGenObject.GenesysGenMakePhysicalBehaviour | GenericGenObject.CgsCoreUniqueId | GenericGenObject.GenesysGenCoronaEnvMapGlow | GenericGenObject.Bool8T | GenericGenObject.FfFfFfF8 | GenericGenObject.GenesysGenPostFxKeyframe | GenericGenObject.GenesysGenNucleusGrantMappingsListMapping | GenericGenObject.GenesysGenGrenadeWeapon | GenericGenObject.GenesysGenVfxSpotEffectSequenceItem | GenericGenObject.GenesysGenWcpathAnimationBehaviour | GenericGenObject.GenesysGenEnvironmentKeyframeHeatHaze | GenericGenObject.GenesysGenGameplayTrigger | number | GenericGenObject.GenesysGenWeaponUpgrade | GenericGenObject.GenesysGenUielementMoviePlayerDimensions | GenericGenObject.GenesysGenPostFxsequenceItem | GenericGenObject.GenesysGenNitrousBurningGameRule | GenericGenObject.GenesysGenImpactDamageGameRule | GenericGenObject.GenesysGenCameraGameplayShakeEffectRotationAxisParams | GenericGenObject.GenesysGenExtraAmmoWeaponUpgrade | GenericGenObject.GenesysGenGameUnlock | GenericGenObject.GenesysGenHeatLevelCopType | GenericGenObject.Float32T | GenericGenObject.GenesysGenUielementScrollableLabelString | GenericGenObject.GenesysGenNucleusEntitlementTag | number | GenericGenObject.GenesysGenUimaterial | GenericGenObject.GenesysGenRoadBlockDefinition | GenericGenObject.GenesysGenEventArenaData | GenericGenObject.T34265a75 | GenericGenObject.GenesysGenThankYouScreenItem | GenericGenObject.GenesysGenUielementMiniMap | GenericGenObject.T0003F683 | GenericGenObject.GenObj | GenericGenObject.GenesysGenCoronaGlow | GenericGenObject.GenesysGenLightBaseFlashPattern | GenericGenObject.T4099F3Ac | number | GenericGenObject.CgsResourceHandle | GenericGenObject.T00075709 | GenericGenObject.GenesysGenScoreViewModel | GenericGenObject.GenesysGenEnvironmentKeyframeWeather | GenericGenObject.GenesysGenTeflonSlickWeapon | GenericGenObject.GenesysGenPerformanceUpgradePackage | GenericGenObject.GenesysGenTextStyleTextStyleLocale | GenericGenObject.T0000301d | GenericGenObject.RwMathVpuMatrix44affine | GenericGenObject.T5b3321F5 | GenericGenObject.GenesysGenMixingGroup | GenericGenObject.Int16T | GenericGenObject.GenesysGenHelicopterWeapon | GenericGenObject.GenesysGenWcvfxBehaviourSpotEffects | GenericGenObject.GenesysGenTextStyle | GenericGenObject.GenesysGenPerk | number | GenericGenObject.GenesysGenWaveSequenceItemFade | GenericGenObject.T000937A3 | GenericGenObject.T00003035 | GenericGenObject.GenesysGenGameUnlockMilestone | GenericGenObject.GenesysGenWcsequenceBehaviour | GenericGenObject.GenesysGenRolloutWeaponData | GenericGenObject.T00045fB1 | GenericGenObject.T000031B6 | GenericGenObject.GenesysGenJumpTimelineController | GenericGenObject.GenesysGenPhysicalDefinitionRigidBodySphereVolume | GenericGenObject.T06A964Cd | GenericGenObject.T0005F70e | GenericGenObject.GenesysGenGameplayTriggerInput | GenericGenObject.T00002fD0 | string | GenericGenObject.GenesysGenPhysicalDefinitionRigidBodyConvexHullVolume | GenericGenObject.GenesysGenFastLaunchWeaponUpgrade | GenericGenObject.GenesysObjCollection | GenericGenObject.T00003027 | GenericGenObject.T0589A977 | GenericGenObject.T0006Cc77 | GenericGenObject.C97eAaDa | GenericGenObject.T8e7d5f21 | GenericGenObject.T0004634a | GenericGenObject.GenesysGenWeaponRechargeData | GenericGenObject.T0006Fa70 | GenericGenObject.T00002fF0 | GenericGenObject.T00003038 | GenericGenObject.GenesysGenWcvfxBehaviourCoronas | GenericGenObject.GenesysGenPhysicalDefinitionRigidBodyCylinderVolume | GenericGenObject.GenesysGenNitrousEarningGameRule | GenericGenObject.RwMathVpuVector3 | GenericGenObject.RwRgba | GenericGenObject.GenesysGenPhysicalExplosionNonRaceCarExplosion | GenericGenObject.T95950d30 | GenericGenObject.RwMathVpuVector2 | GenericGenObject.GenesysGenSilentLaunchWeaponUpgrade | GenericGenObject.GenesysGenPhysicalExplosionGameplayExplosion | GenericGenObject.GenesysGenUielementBase | GenericGenObject.GenesysGenDeviceGrantUpgradePackage | GenericGenObject.GenesysGenEnvironmentKeyframeFog | GenericGenObject.GenesysGenEvent | GenericGenObject.GenesysGenSequenceTimelineController | GenericGenObject.A76d0e28 | number | number | GenericGenObject.GenesysGenUielementPrototypeShape | GenericGenObject.Uint16T | GenericGenObject.GenesysGenWeapon | GenericGenObject.GenesysGenUielementPrototypeImageTintProperties | GenericGenObject.GenesysGenCameraGameplayShakeEffectRotation | GenericGenObject.T000031C4 | GenericGenObject.GenesysGenPostFxKeyframeVignette | GenericGenObject.GenesysGenGameModeScoreOverride | GenericGenObject.GenesysGenWaveSequenceItem | GenericGenObject.GenesysGenScoreViewModelScoreData | GenericGenObject.GenesysGenLightPoint | GenericGenObject.GenesysGenRoadBlockLayerItem | GenericGenObject.GenesysGenSpikeStripBlowoutUpgrade | GenericGenObject.T0000303d | GenericGenObject.T00093793 | GenericGenObject.GenesysGenPhysicalDefinitionRigidBodyCapsuleVolume | GenericGenObject.GenesysGenStoreItem | GenericGenObject.GenesysGenUicolour | GenericGenObject.GenesysGenAddBehaviourSequenceItem | GenericGenObject.T35A6061e | GenericGenObject.GenesysGenVisionMode | GenericGenObject.GenesysGenCameraGameplayShakeEffect | GenericGenObject.GenesysGenApplyVehicleKickSequenceItem | GenericGenObject.Dummy | GenericGenObject.T0006Fa71 | GenericGenObject.GenesysGenSpikeStripWeapon | GenericGenObject.GenesysGenMixerChannel | GenericGenObject.GenesysGenGameplayTriggerOutputSequenceOutput | GenericGenObject.T0005F643 | GenericGenObject.GenesysGenCameraShakeSequenceItem | GenericGenObject.DaDc9b17 | GenericGenObject.T00045eF1 | GenericGenObject.GenesysGenHeatLevel | GenericGenObject.GenesysGenPhysicsSequenceItemPhysicsDoubleValue | GenericGenObject.D0007001 | GenericGenObject.GenesysGenUielementBaseRenderingData | GenericGenObject.T0006Cc2f | GenericGenObject.GenesysGenEnvironmentKeyframeLightRig | GenericGenObject.GenesysGenPhysicalExplosion | GenericGenObject.GenesysGenUielementMainMap | GenericGenObject.T0003F3C4 | GenericGenObject.Int32T | GenericGenObject.GenesysGenGameUnlockList | GenericGenObject.GenesysGenUilayout | GenericGenObject.GenesysGenGameplayMilestoneEntry | GenericGenObject.GenesysGenLightBase | GenericGenObject.GenesysGenMineWeapon | GenericGenObject.F7FfD1F8 | GenericGenObject.GenesysGenEventList | GenericGenObject.GenesysGenUielementPrototypeScrollingTextTextProperties | GenericGenObject.T0007Bc8a | GenericGenObject.GenesysGenEventTriggerSequenceItem | GenericGenObject.GenesysGenEnvironmentTimelineSequenceItem | GenericGenObject.GenesysGenNucleusGrantMappingsList | GenericGenObject.GenesysGenThankyouMapping | GenericGenObject.GenesysGenSoundDistanceFalloff | GenericGenObject.GenesysGenUielementPrototypeLabel | GenericGenObject.Char | GenericGenObject.GenesysGenStorePackList | GenericGenObject.GenesysGenGameRank | GenericGenObject.T96C15369 | GenericGenObject.GenesysGenPhysicalExplosionRaceCarOnGroundExplosion | GenericGenObject.GenesysGenSnapToWorldBehaviour | GenericGenObject.GenesysGenStorePack | GenericGenObject.GenesysGenWcvfxBehaviour | GenericGenObject.GenesysGenPostFxstateColourCubeSettings | GenericGenObject.T000031D2 | GenericGenObject.GenesysGenUielementPrototypeImage | GenericGenObject.GenesysGenGamePack | GenericGenObject.GenesysGenUielementPrototypeScrollingTextString | GenericGenObject.T00002fC8 | GenericGenObject.GenesysGenJammerWeapon | GenericGenObject.GenesysGenSetVisionModeTypeSequenceItem | GenericGenObject.GenesysGenEnvironmentTimeline | GenericGenObject.GenesysGenUielementPrototypeScrollingText | GenericGenObject.GenesysGenUielementPrototypeImageOpacity | GenericGenObject.GenesysGenUielementScrollableLabelTextProperties | GenericGenObject.T0005F393 | GenericGenObject.T0003F715 | GenericGenObject.GenesysGenSpeedbreakerWeapon | GenericGenObject.GenesysGenThermalVisionMode | GenericGenObject.GenesysGenBehaviour | GenericGenObject.GenesysGenUilayoutInstanceParamsTimelineParameters | GenericGenObject.GenesysGenUielementPrototypeLabelTextProperties | GenericGenObject.GenesysGenPostFxstate | GenericGenObject.GenesysGenGameMode | GenericGenObject.GenesysGenUielementBaseTimelineBehaviour | GenericGenObject.GenesysGenCoronaFlare | GenericGenObject.GenesysGenGameplayMilestone | GenericGenObject.GenesysGenChevron | GenericGenObject.GenesysGenSequence | GenericGenObject.RwMathVpuVector4 | GenericGenObject.GenesysGenUielementElementStackTemplate | GenericGenObject.GenesysGenUielementBaseTimeline | GenericGenObject.GenesysGenEnvironmentKeyframeMiniDof | GenericGenObject.T0003F6D5 | GenericGenObject.T00045fAd | GenericGenObject.GenesysGenRoadBlockLayer | GenericGenObject.T000733Ee | GenericGenObject.GenesysGenUilayoutInstanceParamsTransformComponents | GenericGenObject | GenericGenObject.GenesysGenLayoutSequenceItem | GenericGenObject.D7B221Da | GenericGenObject.GenesysGenPhysicsSequenceItem | GenericGenObject.GenesysGenNucleusEntitlementTags | GenericGenObject.GenesysGenWcplaySoundBehaviourPropSurfaceSound | GenericGenObject.CgsCoreStringBase | GenericGenObject.T00003022 | GenericGenObject.GenesysGenGameUnlockEvent | GenericGenObject.GenesysGenUielementPrototypeLabelString | GenericGenObject.GenesysGenGameplayTriggerOutput | GenericGenObject.GenesysGenUielementElementStack | GenericGenObject.GenesysGenBusMixerChannelSequenceItemBusMixerChannelDoubleValue | GenericGenObject.GenesysGenPhysicalDefinitionRigidBodyBoxVolume | GenericGenObject.GenesysGenCarSelectData | GenericGenObject.Uint8T | GenericGenObject.T00002eA1 | GenericGenObject.GenesysGenSmokeScreenWeapon | GenericGenObject.GenesysGenHypoxParticlesWeaponUpgrade | GenericGenObject.GenesysGenPostFxKeyframeStereo3d | GenericGenObject.GenesysGenCarSelectDataSequences | GenericGenObject.T0006Fa8a | GenericGenObject.GenesysGenHudStyleSequenceItem | GenericGenObject.T0005Ab65 | GenericGenObject.GenesysGenWcplaySoundBehaviour | GenericGenObject.GenesysGenPostFxKeyframeBloom | GenericGenObject.GenesysGenBusMixerChannelSequenceItem | GenericGenObject.GenesysGenSequenceItemModulatingDoubleValue | GenericGenObject.GenesysGenWchideBehaviour | GenericGenObject.GenesysGenUielementMoviePlayer | GenericGenObject.Uint32T | GenericGenObject.GenesysGenEnvironmentKeyframe | GenericGenObject.GenesysGenThermalVisionModeProperties | GenericGenObject.GenesysGenSlowMoSequenceItem | GenericGenObject.GenesysGenImpactProtectionGameRule | GenericGenObject.GenesysGenFlashHeadlightsWeapon | GenericGenObject.T000031Ba | GenericGenObject.T35D62d64 | GenericGenObject.GenesysGenEnvironmentKeyframeClouds | GenericGenObject.T0003F65b | GenericGenObject.GenesysGenWcremoveWorldEntityBehaviour | GenericGenObject.GenesysGenGameRule;
    dtype: string;
  }
}
export namespace GenericGenObject {
  export enum E000031Ca {
    EV0 = 0,
    TRANSLATION = 1,
    ROTATION = 2,
    SCALE = 3,
  }
}
export namespace GenericGenObject {
  export enum E00002fC8 {
    EV0 = 0,
    DLC1 = 1,
    EV2 = 2,
    EV3 = 3,
  }
}
export namespace GenericGenObject {
  export enum E00003038 {
    INVALID = 0,
    MATCH = 1,
    LINEAR = 2,
    EXPONENTIAL = 3,
  }
}
export namespace GenericGenObject {
  export enum E0006Cc72 {
    PLAY__ONCE = 0,
    EV1 = 1,
    EV2 = 2,
  }
}
export namespace GenericGenObject {
  export enum E00002fF0 {
    NONE = 0,
    EV1 = 1,
    EV2 = 2,
    EV3 = 3,
  }
}
export namespace GenericGenObject {
  export enum E96C15369 {
    EV0 = 0,
    EV1 = 1,
    EV2 = 2,
  }
}
export namespace GenericGenObject {
  export enum E0006Fa8a {
    NONE = 0,
  }
}
export namespace GenericGenObject {
  export enum E00045fB1 {
    EV0 = 0,
    EV1 = 1,
    EV2 = 2,
    EV3 = 3,
  }
}
export namespace GenericGenObject {
  export enum E4099F3Ac {
    EV0 = 0,
    VERTICAL = 1,
  }
}
export namespace GenericGenObject {
  export enum E0006Fa70 {
    NONE = 0,
  }
}
export namespace GenericGenObject {
  export enum E5b3321F5 {
    NONE = 0,
    EV1 = 1,
    EV2 = 2,
    EV3 = 3,
  }
}
export namespace GenericGenObject {
  export enum E000031D2 {
    EV0 = 0,
    EV1 = 1,
    EV2 = 2,
  }
}
export namespace GenericGenObject {
  export enum ED7B221Da {
    EV0 = 0,
    EV1 = 1,
    EV2 = 2,
  }
}
export namespace GenericGenObject {
  export enum E00003022 {
    NONE = 0,
    LOW = 1,
    NORMAL = 2,
    EXTREME = 3,
  }
}
export namespace GenericGenObject {
  export enum E0003F6D5 {
    GAIN = 0,
    EV1 = 1,
    EV2 = 2,
    EV3 = 3,
    PEAK__FREQUENCY = 4,
    PEAK__GAIN = 5,
    PEAK__Q = 6,
    EV7 = 7,
    LOW__SHELF__GAIN = 8,
    EV9 = 9,
    EV10 = 10,
    EV11 = 11,
    EV12 = 12,
    EV13 = 13,
    EV14 = 14,
    EV15 = 15,
    EV16 = 16,
    EV17 = 17,
    COMPRESSOR__RATIO = 18,
    COMPRESSOR__THRESHOLD = 19,
    VOCALLY_IMPOSE = 20,
    COMPRESSOR__RELEASE = 21,
    EV22 = 22,
  }
}
export namespace GenericGenObject {
  export enum E00003027 {
    NONE = 0,
    ENGINE = 1,
    SKID = 2,
    PLAYER = 3,
    COMPETITOR = 4,
    TRAFFIC = 5,
    UI = 6,
  }
}
export namespace GenericGenObject {
  export enum E34265a75 {
    NONE = 0,
    RANDOM = 1,
    EV2 = 2,
    EV3 = 3,
  }
}
export namespace GenericGenObject {
  export enum E0005Ab65 {
    EV0 = 0,
    DEFAULT = 1,
    EV2 = 2,
    EV3 = 3,
    XRAY = 4,
    EV5 = 5,
  }
}
export namespace GenericGenObject {
  export enum E0003F850 {
    EV0 = 0,
    EV1 = 1,
    EV2 = 2,
    EV3 = 3,
  }
}
export namespace GenericGenObject {
  export enum E0005F393 {
    TAKEDOWN = 0,
    ASSIST = 1,
    SUICIDE = 2,
    TEAMKILL = 3,
    REVENGE = 4,
    FIRST_BLOOD = 5,
    AFTERLIFE = 6,
    DOUBLE_TAKEDOWN = 7,
    TRIPLE_TAKEDOWN = 8,
    TAKEDOWN_FRENZY = 9,
    REVERSE = 10,
    EV11 = 11,
    EV12 = 12,
    COMEBACK = 13,
    TAKENDOWN = 14,
    SPEEDING = 15,
    WEAPON_USED = 16,
    COP_HIT = 17,
    EV18 = 18,
    EV19 = 19,
    EV20 = 20,
    ENTER_COOLDOWN = 21,
    PROP_DAMAGED = 22,
    PROP_DESTROYED = 23,
    TRAFFIC_HIT = 24,
    TRAFFIC_IMMOBILISED = 25,
    EV26 = 26,
    HIT_JUMP = 27,
    JUMP_TAKEDOWN = 28,
    HIT_BLACKSPOT = 29,
    BLACKSPOT_TAKEDOWN = 30,
    HIT_STACK = 31,
    STACK_TAKEDOWN = 32,
    EV33 = 33,
    KEEPING_DRY = 34,
    EV35 = 35,
    HIGH_SPEED = 36,
    ON_RIMS = 37,
    ON_RIMS2 = 38,
    ON_RIMS3 = 39,
    ON_RIMS4 = 40,
    BOOST_PUNCH = 41,
    SLAM_OFFLINE = 42,
    SHUNT_OFFLINE = 43,
    TBONE_OFFLINE = 44,
    SLAM_ONLINE = 45,
    SHUNT_ONLINE = 46,
    EV47 = 47,
    EV48 = 48,
    FIGHT_BONUS = 49,
    WEAPON_HIT = 50,
    HEAD_ON_OFFLINE = 51,
    EV52 = 52,
    AVENGER = 53,
    RESCUER = 54,
    PAYLOAD_TAKEDOWN = 55,
    EV56 = 56,
    PAYLOAD_SPILLED = 57,
    COP_HIT_PAYLOAD = 58,
    INTO_CITY = 59,
    BLINDED = 60,
    SMOKED = 61,
  }
}
export namespace GenericGenObject {
  export enum E00002eA1 {
    EV0 = 0,
    EV1 = 1,
    EV2 = 2,
    EV3 = 3,
    EV4 = 4,
    EV5 = 5,
  }
}
export namespace GenericGenObject {
  export enum E00045fAd {
    EV0 = 0,
    EV1 = 1,
  }
}
export namespace GenericGenObject {
  export enum E00045eF1 {
    EV0 = 0,
    EV1 = 1,
    EV2 = 2,
    EV3 = 3,
  }
}
export namespace GenericGenObject {
  export enum E00003035 {
    EV0 = 0,
    HIGH_COST = 1,
  }
}
export namespace GenericGenObject {
  export enum E0005F70e {
    TIME = 0,
    SCORE = 1,
  }
}
export namespace GenericGenObject {
  export enum E70F4BbE0 {
    LEFT = 0,
    EV1 = 1,
    EV2 = 2,
    FULL = 3,
  }
}
export namespace GenericGenObject {
  export enum E0003F715 {
    NICKNAME_VIOLATION = 0,
    EV1 = 1,
    DRAG = 2,
    ENGINE__LOAD = 3,
    THROTTLE = 4,
  }
}
export namespace GenericGenObject {
  export enum E0006Cc2f {
    EV0 = 0,
    EV1 = 1,
  }
}
export namespace GenericGenObject {
  export enum E0005F643 {
    DEFAULT = 0,
    WAITING = 1,
    PATROLLING = 2,
    ESCAPING = 3,
    CHASING = 4,
    WAITING__LIGHTS = 5,
    IDLE__LIGHTS = 6,
    RHINO = 7,
  }
}
export namespace GenericGenObject {
  export enum EA76d0e28 {
    NONE = 0,
    EV1 = 1,
    BOLD = 2,
    EV3 = 3,
    EV4 = 4,
    EV5 = 5,
    GLOW = 6,
    EV7 = 7,
  }
}
export namespace GenericGenObject {
  export enum ED0007001 {
    NONE = 0,
    EV1 = 1,
    EV2 = 2,
    EV3 = 3,
  }
}
export namespace GenericGenObject {
  export enum E000031C4 {
    EV0 = 0,
    EV1 = 1,
    EV2 = 2,
    EV3 = 3,
    EV4 = 4,
    EV5 = 5,
  }
}
export namespace GenericGenObject {
  export enum E0003F683 {
    TIME = 0,
    BINDING = 1,
  }
}
export namespace GenericGenObject {
  export enum E0000301d {
    NEAR = 0,
    MID = 1,
    FAR = 2,
    EV3 = 3,
  }
}
export namespace GenericGenObject {
  export enum E95950d30 {
    EV0 = 0,
    EV1 = 1,
    EV2 = 2,
    EV3 = 3,
    EV4 = 4,
    EV5 = 5,
    EV6 = 6,
    EV7 = 7,
    EV8 = 8,
    EV9 = 9,
    EV10 = 10,
    EV11 = 11,
    EV12 = 12,
  }
}
export namespace GenericGenObject {
  export enum E0006Fa71 {
    NONE = 0,
  }
}
export namespace GenericGenObject {
  export enum E06A964Cd {
    EV0 = 0,
    VERTICAL = 1,
  }
}
export namespace GenericGenObject {
  export enum E00075709 {
    EV0 = 0,
    EV1 = 1,
  }
}
export namespace GenericGenObject {
  export enum E0004634a {
    DEDUCTED__SHIELD = 0,
    EV1 = 1,
  }
}
export namespace GenericGenObject {
  export enum E00002fD0 {
    EV0 = 0,
    ONLINE = 1,
    EV2 = 2,
    EV3 = 3,
  }
}
export namespace GenericGenObject {
  export enum E000031B6 {
    EV0 = 0,
    EV1 = 1,
    EV2 = 2,
  }
}
export namespace GenericGenObject {
  export enum E0007Bc8a {
    NONE = 0,
    EV1 = 1,
  }
}
export namespace GenericGenObject {
  export enum E0c966a95 {
    EV0 = 0,
    EV1 = 1,
    BOTH = 2,
    EV3 = 3,
    ONLINE = 4,
  }
}
export namespace GenericGenObject {
  export enum E000937A3 {
    DEFAULT = 0,
    HELICOPTER = 1,
  }
}
export namespace GenericGenObject {
  export enum E35D62d64 {
    FADE = 0,
    MOVE = 1,
    EV2 = 2,
    EV3 = 3,
    SCALE = 4,
    EV5 = 5,
    EV6 = 6,
    EV7 = 7,
    EV8 = 8,
    EV9 = 9,
    EV10 = 10,
    EV11 = 11,
    EV12 = 12,
    TINT = 13,
    EV14 = 14,
    EV15 = 15,
    EV16 = 16,
    EV17 = 17,
    EV18 = 18,
  }
}
export namespace GenericGenObject {
  export enum E0006Cc77 {
    EV0 = 0,
    EV1 = 1,
    EV2 = 2,
    EV3 = 3,
    EV4 = 4,
  }
}
export namespace GenericGenObject {
  export enum E000031Ba {
    EV0 = 0,
    EV1 = 1,
    EV2 = 2,
    EV3 = 3,
    EV4 = 4,
    EV5 = 5,
    EV6 = 6,
    EV7 = 7,
    EV8 = 8,
  }
}
export namespace GenericGenObject {
  export enum E00093793 {
    EV0 = 0,
    EV1 = 1,
  }
}
export namespace GenericGenObject {
  export enum EDaDc9b17 {
    EV0 = 0,
    EV1 = 1,
    EV2 = 2,
    EV3 = 3,
    EV4 = 4,
    EV5 = 5,
    EV6 = 6,
    EV7 = 7,
    EV8 = 8,
  }
}
export namespace GenericGenObject {
  export enum EF7FfD1F8 {
    LEFT = 0,
    EV1 = 1,
    EV2 = 2,
    FULL = 3,
  }
}
export namespace GenericGenObject {
  export enum E0003F65b {
    MULTIPLY = 0,
    OFFSET = 1,
    ABSOLUTE = 2,
  }
}
export namespace GenericGenObject {
  export enum E35A6061e {
    LEFT = 0,
    EV1 = 1,
    EV2 = 2,
    FULL = 3,
  }
}
export namespace GenericGenObject {
  export enum E000733Ee {
    SOURCE = 0,
    EV1 = 1,
    PERCEIVES_SEVERAL = 2,
    EV3 = 3,
    EV4 = 4,
    EV5 = 5,
    EV6 = 6,
  }
}
export namespace GenericGenObject {
  export enum E8e7d5f21 {
    NONE = 0,
    RANDOM = 1,
    EV2 = 2,
    EV3 = 3,
  }
}
export namespace GenericGenObject {
  export enum EC97eAaDa {
    EV0 = 0,
    EV1 = 1,
    EV2 = 2,
  }
}
export namespace GenericGenObject {
  export enum E0000303d {
    NONE = 0,
    POWER = 1,
    MULTIPLY = 2,
  }
}
export namespace GenericGenObject {
  export enum E0589A977 {
    FADE = 0,
    MOVE = 1,
    EV2 = 2,
    EV3 = 3,
    SCALE = 4,
    EV5 = 5,
    EV6 = 6,
    EV7 = 7,
    EV8 = 8,
    EV9 = 9,
    EV10 = 10,
    EV11 = 11,
    EV12 = 12,
    TINT = 13,
    EV14 = 14,
    EV15 = 15,
    EV16 = 16,
    EV17 = 17,
    EV18 = 18,
  }
}
export namespace GenericGenObject {
  export enum E0003F3C4 {
    LOADED = 0,
    STREAMED = 1,
    EV2 = 2,
    DECAY_EXCEPTIONALLY = 3,
    EV4 = 4,
  }
}
