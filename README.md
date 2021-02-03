# ictf Round 7
## Sanity Check
**Description**
> Welcome to Round 7! DM flags to me to get points, and rise up on the leaderboard! Have fun and enjoy Round 7!

**Attachments**

Here's your flag: `ictf{Round_7_Sanity_Check}`

**Category**

Misc

**Explanation**

Just submit `.flag ictf{Round_7_Sanity_Check}`
\
\
\
## Inspector

**Description**

Look at our website! Can you inspect it?

**Attachments**

https://imaginary.ml/

**Category**

Web
\
\
\
## null
**Description**
> Have a look at this message I found in an old chest. I also found its key. `key = [24, 28, 110, 126, 145, 200, 209, 222, 231, 332, 447, 460, 472, 476, 480, 569, 591, 629, 633, 650, 671, 695, 696, 699, 706, 833].` Can you decrypt it? 

**Attachments**

[ciphertext](https://github.com/ainzs-evil-twin/ictf-Feb-2021/blob/main/null/Corrosion.txt)

**Category**

Crypto

**Explanation**

The key refers to the `i`th letter of the string.
```python
key = [24, 28, 110, 126, 145, 200, 209, 222, 231, 332, 447, 460, 472, 476, 480, 569, 591, 629, 633, 650, 671, 695, 696, 699, 706, 833]
s = 'CorrosionIsTheProcessThatCanDeteriorateTheQualityOfAMaterialOrChangeItToSomeOtherMaterialEntirelyDueToTheEffectsOfTheSurroundingsItCanGraduallyDestroyMaterialsByChemicalProcessesCausedNaturallyByTheEnvironmentItIsASignificantConcernForBiomaterialsToBeCorrosionResistantBecauseCorrosionCanCauseAMaterialToLoseItsOriginalFunctionalityAndBringAboutModificationsOnTheSurfaceItMightAlsoLeadToTheReleaseOfMetalIonsIntoTheBodyWhichCanResultInAllergicResponsesAndSometimesACarcinogenicResponseInWorstCaseScenariosCorrosionInAMetallicBiomaterialMayChangeThePhAndOxygenContentsOfTheSurroundingsAndAChangeInBehaviourMayOccurInSuchConditionsHenceThereShouldBeALimitToHowMuchCorrosionIsAllowedInAWorkingBiomaterialWeCanConcludeThatTheCorrosionProcessIsOneOfTheMostImportantMediatorsOfTheTissueResponseToMetallicBiomaterialsAndADecentUnderstandingAndAccurateEvaluationOfTheCorrosionBehaviourIsNecessaryInOrderToDesignBiomaterialsOftentimesNobleMetalsAndMetalsWhichDevelopInertOxideLayerOverTheirSurfacesAreSeenBeingUsedInMedicalDevicesWhereAlmostNoCorrosionIsTolerableOnTheOtherHandSometimesWeNeedBiomaterialsWhichAreResorbableAndDegradeGraduallyOverAPeriodOfTimeSoThatTheyCanBeReplacedWithNaturalTissuesInSuchCasesCorrosionIsANecessaryEvilAndCanBeUsedInOurFavour'
t = ''
for k in key:
    t += s[k-1]
print(t)
```
This prints out `ancientcryptoisfascinating` so we can just submit `.flag ictf{ancientcryptoisfascinating}`.
<!-- ## Name
**Description**
>

**Attachments**


**Explanation**


**Category** -->