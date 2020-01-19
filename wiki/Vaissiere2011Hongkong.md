## generalities

On the basis of the acoustic theory of speech production, this paper aims to propose a set of focal vowels characterized by an almost complete merging of two adjacent formants: F1 and F2, F2 and F3, and F3 and F4 (sometimes F4 and F5 for some speakers).
(a i u y)

These reference vowels constitute a **subset** of Jones's Cardinal Vowels (CVs); they are the only vowels that can be called “quantal” in Stevens‟ sense.
(cf Stevens, what is quantal ??? A lire absolument.focal (“quantal”) in acoustic terms)

Formant merging creates a vowels-pecific sharp concentration of spectral energy in a narrow region of the frequency scale. This acoustic result results from very specific articulatory configurations and entails special perceptual characteristics.
(concentration, acoustics and perception)
.

## IPA

The target for a vowel seems to be much easier to describe in acoustic rather that in articulatory terms. A phonemically defined contrast involves even more than two gestures.

- Peterson and Barnet's formant plot
  <img src="img/2019-06-10-15-21-49.png">

Jones‟s cardinal chart aims to characterize the **phonetic** quality of the vowels. In his Outline of English Phonetics [19], Jones claims that “a good ear can distinguish well over fifty vowels, exclusive of nasalized vowels, vowels pronounced with retroflex modification, etc.”

The Cardinal Vowels (CVs) (eight primary CVs and eight secondary CVs (reference points)

any vowel quality, from any language, can be described by interpolating between the reference points. The CVs are widely employed to this day.
<img src="img/2019-06-10-15-28-15.png">

Moreover, according to Jones, the CVs can only be learnt through oral instruction from a teacher who knows them.

## Acoustics

### focal vowels comparison

The CVs have not been explicitly related to their acoustic characteristics (see however [26]).

.

.

<img src="img/2019-06-10-15-34-56.png">
<img src="img/2019-06-10-15-35-03.png">
### F2 prime
#### IPA formants (F3?)
The vertical F1 corresponds to vowel “height”: the “lower” the vowel, the higher the F1. The horizontal F2 axis corresponds to tongue advancement: the more “back” the vowel, the lower the F2 frequency value [23].

The F1/F2 plot offers a fairly good visual separation of the vowels. But the three articulatory dimensions of the IPA chart (or of Stevens and Fant‟s models, shown in Fig. 4) are reduced to two dimensions, raising the issue of whether two dimensions, such as the two first formant frequency values, can provide an adequate acoustic representation of vowels.

#### answers of formants sufficiency

- when in the low frequency range

The answer depends on the location of the concentration of energy on the frequency scale [10]. When the energy is concentrated in the low frequencies (say, under 1000 Hz), the first two formants, F1 and F2, are sufficient for creating the quality of the back CVs.

By the law of acoustics, the upper formants of these back vowels are of weak intensity, and therefore carry little perceptual weight (if any).

The first two grouped formants are even perceptually equivalent to a single formant, so that back vowels can be synthesized using a single formant [10]

- when not in the low frequency range

several formants above F1 are of comparable strength, and have a perceptual weight.

In languages that contrast front vs. mid, round vs. unrounded vowels, F3 plays a critical role. In French, for example, F1 and F2 for /i/ and /y/ can be similar for some speakers (see Figure 7 for an example). F1 and F2 have proved insufficient for imitating the phonetic values of the non-back vowels.

#### F2 prime

F2‟ (F2 prime) is an aggregate computed from F2 and higher formants. The F2‟ frequency substitutes a single peak to all formants above F1, aiming to mirror their perceptual integration [4], [6].

F1 is fixed, and is equal to the original F1 frequency of the vowel; F2‟ is variable at will. **How to test**

F2 prime is called a perceptually relevant formant value

<img src="img/2019-06-10-15-39-56.png">

- Generally, when F2 is above 2000 Hz (as in [i e]), F2‟ is higher than F2; it is close to F4 (or even higher) for [i] in languages like Swedish and French where the vowel is characterized by the grouping of F3 and F4 (like the cardinal [i])
- It lies inbetween F2 and F3 for [y], for which F2 and F3 are grouped. When F2 is below 1000 Hz, F1 and F2 are bunched together, and F2‟ is close to F2 (sometimes close to F1 for [u]).

F2‟ therefore serves a dimension-reduction function, from four formants to just two.

Vowel mapping based on F1 vs. F2‟ is more successful than F1 vs. F2 in separating the front high and mid rounded and unrounded vowels [12].

Synthesis based on F1 and F2‟ is not very natural for front vowels, however [15].

F2‟ corresponds to the best approximation of the upper formants by a single value, but it is not really perceptually equivalent to the original.

On the other hand, the first four formants reproduce the quality of the vowels with very high accuracy.

## modelisation

The relationships between the articulatory space (the VT profiles), the acoustic space (the formant frequencies), and the perceptual space are complex and not linear [35].

Modeling is based on the source-filter theory, i.e. the principle of the independence between the (voice) source at the glottis (phonation) and the filtering by supraglottal cavities (articulation) [7], [11], [35]

a constriction near a pressure node lowers the formant frequency, whereas a constriction near a pressure antinode raises it.

node vs antinode : https://www.britannica.com/science/pressure-node
https://www.acs.psu.edu/drussell/Demos/StandingWaves/StandingWaves.html
https://www.quora.com/What-are-pressure-nodes-and-antinodes

- How the modelisation works :
  Any mid-sagittal profile (obtained from X-ray or MRI data) can be converted into a cross-sectional area function where the VT is represented by a series of cylindrical sections of averaging area along a straight axis from the glottis to the lips. The area function preserves the resonance characteristics of the VT [11]; the area function is transformed into an acoustic spectral transfer function and the resulting sound is generated and can be heard.
- some details and use for perceptive test
  If desired, the area function is able to reproduce the details seen on mid-sagittal profiles; the sagittal profiles may be simplified by the concatenation of simple tubes, for example two connected tubes for [i], [y], [ɑ] or [a], and four connected tubes for [o], [ɔ] and [u][12], [35]. To estimate the sensitivity of each formant to a small or large articulatory change [14], each section of the area function can be **slightly** perturbed (constricted or expanded), and the transfer function calculated. The acoustic characteristics of the resulting signal can be then compared with those of the original sound (if available). The synthesized signal can be used as stimulus for perception tests (for details see [27]).

## nomograms and tubes

A nomogram is a very useful way to display the acoustic consequences of modifying constriction position, constriction size, and degree of lip opening, as illustrated in Fig. 4. Fant [11] has shown that the vocal tract transfer function estimated from X-ray data corresponding to vowels can be quite accurately calculated from a four-tube, three-parameter model [36].

Note that the three parameters used to specify the vowels are not the same as those three parameters used in the IPA chart

- The first parameter is the distance from the glottis to the center of the constriction,
- the second is its area, and
- the third is the length-to-opening ratio of the lip tube area. [i], [u] and [ɑ] correspond respectively to a constriction on the front (palatal), mid (velar) and back (pharyngeal) parts of the VT.

In Figure 4, the constriction size is fixed and the two varying parameters are (i) the location of the constriction, from glottis (on the right) to lips (on the left) and (ii) the lip configuration with two states, constricted and opened.

Area function corresponding to Fant‟s second model. The vertical arrow represents the location of the maximum tongue constriction in the VT that is varied from glottis to lips. The minimal cross-section area at the constriction is fixed here to 0.65 cm². (b): the corresponding nomogram. Straight and dotted lines correspond respectively to open (in the solid lines) and rounded/protruded lips (in the dashed lines). Black, blue and green colors refer respectively to F1, F2 and F3.

<img src="img/2019-06-10-15-52-00.png">

Human speakers can only produce vowels over a range that is less than half that the range represented in Fant's nomograms [24].

There are basically three regions.

- constriction is near the front end of the VT, the distance between F1 and F2 is much larger than the distance between F2 and F3. This region corresponds to i- and e-like sounds (zone “I” in Fig. 4).
- it is close to the glottis, F1 is high and the region corresponds to open sounds (zone “A”).
- When the lips are rounded, there is a region where the distance between F1 and F2 is much smaller than the distance between F2 and F3, and F1 and F2 are low in frequency (zone “U”).
  The regions where F2 is high and therefore close to F3 (zone I) or F1 and F2 converge (zone A and zone U) correspond to quantal regions, as described by Stevens [34].

## Acoutisc definitions

Figure 5 represents the same nomogram as in Figure 4, but the points where two formants converge are singled out by circles.

**As clearly stated in Stevens‟s Quantal Theory (QT), when the frequency of a formant is maximally high or low, it usually goes hand in hand with formant convergence.**

**when two formants converge, their amplitude increases by 6 dB per halving their distance [11] creating a sharp spectral salience in a well-defined frequency range**

Formant merging may be favored because it corresponds to articulatory stability, as stated by the QT, or for auditory reasons.

<img src="img/2019-06-10-15-56-55.png">

### i

- When the constriction is very fronted, i.e. in the prepalatal region, F3 reaches a maximum (transcribed as ⇑)
  F3 is affiliated to the front cavity (indicated by underlining in our notation), which is made as short as possible
  Articulatory modeling shows that the tongue has to be placed parallel to the palate to create a halfwave-length resonance, the type of resonance which creates the highest frequency.
  F2 is not maximal. The vowel fits well to the CVs uttered by PL and DJ(????), and to the /i/ of French [37] and Swedish [12].

Gendrot, et al. [17] compared the four first formant frequencies of /i/ in continuous speech in English, German, French, Spanish, Portuguese, Arabic and Mandarin. Their results indicate that French /i/ has the lowest F1, the highest F3 and the highest F4, as well as the smallest distance between F3 and F4 (see Table 1).

<img src="img/2019-06-10-16-00-23.png">

This reference vowel does not seem very common, maybe because it requires a high articulatory precision.

The next figure illustrates two types of /i/, as pronounced by Ladefoged (the sounds are available on the Internet).
left one much sharper
<img src="img/2019-06-10-16-00-38.png">

Note that focal vowels seem to be as sensitive to coarticulation as non-focal vowels [31][36]. Figure 7 illustrates the spectrograms corresponding to the central portion of the vowel [i], in isolation, and in uvular context.

**When the vowel is surrounded by [ʁ], the length of the front cavity increases, and the front cavity resonance (here: F3) tends to decrease in frequency. F1 tends to increase and /i/ sounds close to [e].**

<img src="img/2019-06-10-16-01-54.png">

### y

(F2F3) 1900Hz corresponds to the narrowest passage in the prepalatal region (the second highest circle in Fig. 4), where F3 is most sensitive to rounding, and the lips are rounded.

**In the transition from [i] to [y], F2 becomes a resonance of the front cavity.**

Languages contrasting [i] and [y] seem to prefer a prepalatal position for both [41].

**(F2F3) 1900Hz does not correspond to Jones‟s /y/, nor to Swedish or German, but clearly corresponds to the rendition of cardinal vowel /y/ by PL and to French /y/.**

### u

F1F2 clustering corresponds to the lowest possible concentration of energy. F1 and F2 correspond to two Helmholtz resonances, the type of resonances that produces the lowest resonance frequency. It requires two strong constrictions, at the lip and at the middle of the mouth.
The vowel corresponds to DJ‟s and PL‟s CV [u].

### back a

It corresponds to the highest **possible clustering** of the two first formants.

**A constriction at the root of the tongue leads to an even higher F1 and an /æ /like sound [13]**, **with a separation of F1 and F2** (see Fig. 1).

### o and ɔ

As stated by DJ, the two other back vowels may be created as equidistant from Cardinal C8 [u] and Cardinal C5 [ɑ].

**For keeping F1F2 clustered, the tongue constriction has to move back from C8 to C5 synchronously with a delabialization gesture(????).**

### ɚ

[ɚ]= (F2⇓F3) 1500Hz is not among the CVs. Nonetheless, it represents an extreme in terms of a low F3, which gets as low as 1,500 Hz. The production of (F2⇓F3) 1500Hz is achieved by

- a constriction in the pharyngeal region
- plus lip rounding and
- a bunching of the tongue.

Palatal retroflexion is one gesture that lowers F3 (alveolar retroflexion lowers F4) [11].

The three necessary constrictions correspond to the three points along
the vocal tract where the volume velocity nodes of F3 are located [7].

### others

The three other front primary vowels C2, C3 and C4 (e ɛ a) do not correspond to a less constricted VT [13]. These vowels are more difficult to define in acoustic terms. They have in common two peaks of equal strength above F1 and no focalization.

## concluding remarks

A traditional phonological feature (such as round or back) is generally described by a defining gesture: lip rounding for the feature round, or tongue retraction for the feature back. Both lip rounding and tongue retraction lead to the lengthening of the front cavity, thus to the lowering of the formants associated with that cavity.

The two gestures have to work in strong synchrony, for the manipulation of F3 for the front vowels (spreading and fronting), or to keep F1 and F2 clustered for the back vowels (rounding and backing): the more back the vowels, the less rounded the lips (4 different phonetic degrees of rounding for the back vowels to keep F1F2 clustered ????).

Schwarz and coworkers [32] found that focalization led to more stable patterns in discrimination tasks.

Are they any easier to recognize than other vowels? Are their coarticulatory properties any different? What is their distribution among the world‟s languages?

As for the distribution across languages, focal (“quantal”) vowels do not appear to be particularly common.

According to Ladefoged [22], the Ngwe language of West Africa has 8 vowels which are rather similar to the 8 primary cardinal vowels.

French is often cited as having vowels close to the CVs (note, however, that younger generations have lost the opposition between [ɑ] and [a]; the opposition between [œ] and [ø] is currently weakening).
