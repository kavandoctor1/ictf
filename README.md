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




## Inspector

**Description**

Look at our website! Can you inspect it?

**Attachments**

https://imaginary.ml/

**Category**

Web

**Explanation**

If you view page source on the website, you find a comment of the form 
```html
<!-- The flag is ictf{1nsp3ct_th3_s0urc3_c0de} -->
```
Therefore, we can just submit `.flag ictf{1nsp3ct_th3_s0urc3_c0de}`.  




## Null
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




## where is the SUGAR...

**Description**

I seem to have Lost my sugaR... can yoU find the differenCe?

**Attachments**

http://oreos.ctfchallenge.ga/

**Category**

Web Explotation

**Explanation**

Doing `curl -i` on the url, shows that it seems to send a cookie of the form `sugar=False`.  
Therefore, we can try and override that cookie by doing something of the form:
```curl -L -v --cookie "sugar=True" -i http://oreos.ctfchallenge.ga/```
where the -L is to follow redirects. This leads us to a webpage of the form:
```html
<!DOCTYPE html>
<html lang=en>
  <head>
    <title>i can make my cookie now :D</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel= "stylesheet" type= "text/css" href= "/static/css/theme.css">
    <script src="/static/js/script.js"></script>
    <link rel="shortcut icon preconnect" href="/static/favicon.ico">
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Langar&display=swap" rel="stylesheet">
  </head>
  <body>
      <flag>ictf{c00k13s_@re_S0oO_co0L}</flag>
  </body>
</html>
```
Therefore we can just submit `.flag ictf{c00k13s_@re_S0oO_co0L}`.



## A Stegosaurus?
**Description**

What a cool picture of a dinosaur :)

**Attachments**

https://fdownl.ga/A7C8E8F4CD

**Category**

Forensics

**Explanation**  

Put the image into a hex editor like https://hexed.it/, and towards the end you find the flag in the hex: ictf{w0w_st3gan0graphy!} so you can just submit `.flag ictf{w0w_st3gan0graphy!}`  


 ## adminpassword
**Description**  
>My friend Toby said this website had the most difficult protection in the world! Apparently, something is hidden! Could you help me break in?  


**Attachments**  
http://oreos.ctfchallenge.ga:1337/  


**Category**  
Web Explotation


**Explanation**  

If you open the source code, you find a comment in the HTML:
```html
<!-- <input name='password' placeholder='Password' type='password' value=""> -->
```

If you inspect source, and uncomment this line of HTML, you get a second input in the form.  
Now, using the name of the challenge, you can enter `admin` for the username, and `password` for the password.  
This gives a flag of ictf{1nv1sIbl3_fl@g5} you can just submit `.flag ictf{1nv1sIbl3_fl@g5}`

## nucleotides

**Description**

Nucleotides are the subunits which make up the DNA. The 4 kinds of nucleotides in the DNA are distinguished by their nitrogen heterocycle substituents: adenine(A), cytosine(C), guanine(G), and thymine(T).
In a parallel universe, the DNA is composed of 8 kinds of nucleotides instead of 4: A, C, G, K, M, R, T, and U. Find out how many unique strands of length 8 (may contain repeated nucleotides) are possible in this universe. Also, find the 250th strand (counting starts from 1) in this set, after this set is sorted alphabetically.

**Attachments**

https://github.com/ainzs-evil-twin/ictf-Feb-2021/blob/main/nucleotides/README.md

**Category**

Programming/Maths

**Explanation**

For each of the 8 characters in the DNA string, there are 8 options to choose from.  
Therefore, there are a total of `8*8*8*8*8*8*8*8 = 8^8 = 16777216` unique strands of length 8.
Therefore the flag is ictf{16777216_AAAAAKUC} and we can just submit `.flag ictf{16777216_AAAAAKUC}`.