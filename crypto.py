key = [24, 28, 110, 126, 145, 200, 209, 222, 231, 332, 447, 460, 472, 476, 480, 569, 591, 629, 633, 650, 671, 695, 696, 699, 706, 833]
s = 'CorrosionIsTheProcessThatCanDeteriorateTheQualityOfAMaterialOrChangeItToSomeOtherMaterialEntirelyDueToTheEffectsOfTheSurroundingsItCanGraduallyDestroyMaterialsByChemicalProcessesCausedNaturallyByTheEnvironmentItIsASignificantConcernForBiomaterialsToBeCorrosionResistantBecauseCorrosionCanCauseAMaterialToLoseItsOriginalFunctionalityAndBringAboutModificationsOnTheSurfaceItMightAlsoLeadToTheReleaseOfMetalIonsIntoTheBodyWhichCanResultInAllergicResponsesAndSometimesACarcinogenicResponseInWorstCaseScenariosCorrosionInAMetallicBiomaterialMayChangeThePhAndOxygenContentsOfTheSurroundingsAndAChangeInBehaviourMayOccurInSuchConditionsHenceThereShouldBeALimitToHowMuchCorrosionIsAllowedInAWorkingBiomaterialWeCanConcludeThatTheCorrosionProcessIsOneOfTheMostImportantMediatorsOfTheTissueResponseToMetallicBiomaterialsAndADecentUnderstandingAndAccurateEvaluationOfTheCorrosionBehaviourIsNecessaryInOrderToDesignBiomaterialsOftentimesNobleMetalsAndMetalsWhichDevelopInertOxideLayerOverTheirSurfacesAreSeenBeingUsedInMedicalDevicesWhereAlmostNoCorrosionIsTolerableOnTheOtherHandSometimesWeNeedBiomaterialsWhichAreResorbableAndDegradeGraduallyOverAPeriodOfTimeSoThatTheyCanBeReplacedWithNaturalTissuesInSuchCasesCorrosionIsANecessaryEvilAndCanBeUsedInOurFavour'
t = ''
for k in key:
    t += s[k-1]
print(t)
