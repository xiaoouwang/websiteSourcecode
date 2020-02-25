---
title: Start Web Scraping (2/10) | Advanced Parsing
subtitle: Advanced parsing
summary: PARSING & DOM TRAVERSAL & LAMBDA FUNCTION
authors:
- Xiaoou WANG
tags: ["Web Scraping in 10 lessons","Python"]
categories: ["Web Scraping","Python"]
date: "2020-01-04"
# lastMod: "2020-01-02"
featured: false
draft: false
# markup: blackfriday
# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: ""
  focal_point: ""

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references
#   `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: ["Python"]
---
<!-- {{% toc %}} -->

## Find all the span tags with the following attributes (class equal to green) = person names


```python
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html, "html.parser")
```


```python
# all the names are in span tag of class green, in order of appearance in the text
# bs.find_all(tagName, tagAttributes)
# attributes are dictionary
nameList = bs.findAll('span', {'class': 'green'})
for name in nameList:
    print(name.get_text())
```

    Anna
    Pavlovna Scherer
    Empress Marya
    Fedorovna
    Prince Vasili Kuragin
    Anna Pavlovna
    St. Petersburg
    the prince
    Anna Pavlovna
    Anna Pavlovna
    the prince
    the prince
    the prince
    Prince Vasili
    Anna Pavlovna
    Anna Pavlovna
    the prince
    Wintzingerode
    King of Prussia
    le Vicomte de Mortemart
    Montmorencys
    Rohans
    Abbe Morio
    the Emperor
    the prince
    Prince Vasili
    Dowager Empress Marya Fedorovna
    the baron
    Anna Pavlovna
    the Empress
    the Empress
    Anna Pavlovna's
    Her Majesty
    Baron
    Funke
    The prince
    Anna
    Pavlovna
    the Empress
    The prince
    Anatole
    the prince
    The prince
    Anna
    Pavlovna
    Anna Pavlovna



```python
# find tags in a list War and Peace is h1
titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])
print([title.get_text() for title in titles])
```

    ['War and Peace', 'Chapter 1']



```python
# red texts are dialogues
allText = bs.find_all('span', {'class':{'green', 'red'}})
print([text for text in allText])
```

    [<span class="red">Well, Prince, so Genoa and Lucca are now just family estates of the
    Buonapartes. But I warn you, if you don't tell me that this means war,
    if you still try to defend the infamies and horrors perpetrated by
    that Antichrist- I really believe he is Antichrist- I will have
    nothing more to do with you and you are no longer my friend, no longer
    my 'faithful slave,' as you call yourself! But how do you do? I see
    I have frightened you- sit down and tell me all the news.</span>, <span class="green">Anna
    Pavlovna Scherer</span>, <span class="green">Empress Marya
    Fedorovna</span>, <span class="green">Prince Vasili Kuragin</span>, <span class="green">Anna Pavlovna</span>, <span class="green">St. Petersburg</span>, <span class="red">If you have nothing better to do, Count [or Prince], and if the
    prospect of spending an evening with a poor invalid is not too
    terrible, I shall be very charmed to see you tonight between 7 and 10-
    Annette Scherer.</span>, <span class="red">Heavens! what a virulent attack!</span>, <span class="green">the prince</span>, <span class="green">Anna Pavlovna</span>, <span class="red">First of all, dear friend, tell me how you are. Set your friend's
    mind at rest,</span>, <span class="red">Can one be well while suffering morally? Can one be calm in times
    like these if one has any feeling?</span>, <span class="green">Anna Pavlovna</span>, <span class="red">You are
    staying the whole evening, I hope?</span>, <span class="red">And the fete at the English ambassador's? Today is Wednesday. I
    must put in an appearance there,</span>, <span class="green">the prince</span>, <span class="red">My daughter is
    coming for me to take me there.</span>, <span class="red">I thought today's fete had been canceled. I confess all these
    festivities and fireworks are becoming wearisome.</span>, <span class="red">If they had known that you wished it, the entertainment would
    have been put off,</span>, <span class="green">the prince</span>, <span class="red">Don't tease! Well, and what has been decided about Novosiltsev's
    dispatch? You know everything.</span>, <span class="red">What can one say about it?</span>, <span class="green">the prince</span>, <span class="red">What has been decided? They have decided that
    Buonaparte has burnt his boats, and I believe that we are ready to
    burn ours.</span>, <span class="green">Prince Vasili</span>, <span class="green">Anna Pavlovna</span>, <span class="green">Anna Pavlovna</span>, <span class="red">Oh, don't speak to me of Austria. Perhaps I don't understand
    things, but Austria never has wished, and does not wish, for war.
    She is betraying us! Russia alone must save Europe. Our gracious
    sovereign recognizes his high vocation and will be true to it. That is
    the one thing I have faith in! Our good and wonderful sovereign has to
    perform the noblest role on earth, and he is so virtuous and noble
    that God will not forsake him. He will fulfill his vocation and
    crush the hydra of revolution, which has become more terrible than
    ever in the person of this murderer and villain! We alone must
    avenge the blood of the just one.... Whom, I ask you, can we rely
    on?... England with her commercial spirit will not and cannot
    understand the Emperor Alexander's loftiness of soul. She has
    refused to evacuate Malta. She wanted to find, and still seeks, some
    secret motive in our actions. What answer did Novosiltsev get? None.
    The English have not understood and cannot understand the
    self-abnegation of our Emperor who wants nothing for himself, but only
    desires the good of mankind. And what have they promised? Nothing! And
    what little they have promised they will not perform! Prussia has
    always declared that Buonaparte is invincible, and that all Europe
    is powerless before him.... And I don't believe a word that Hardenburg
    says, or Haugwitz either. This famous Prussian neutrality is just a
    trap. I have faith only in God and the lofty destiny of our adored
    monarch. He will save Europe!</span>, <span class="red">I think,</span>, <span class="green">the prince</span>, <span class="red">that if you had been
    sent instead of our dear <span class="green">Wintzingerode</span> you would have captured the
    <span class="green">King of Prussia</span>'s consent by assault. You are so eloquent. Will you
    give me a cup of tea?</span>, <span class="green">Wintzingerode</span>, <span class="green">King of Prussia</span>, <span class="red">In a moment. A propos,</span>, <span class="red">I am
    expecting two very interesting men tonight, <span class="green">le Vicomte de Mortemart</span>,
    who is connected with the <span class="green">Montmorencys</span> through the <span class="green">Rohans</span>, one of
    the best French families. He is one of the genuine emigres, the good
    ones. And also the <span class="green">Abbe Morio</span>. Do you know that profound thinker? He
    has been received by <span class="green">the Emperor</span>. Had you heard?</span>, <span class="green">le Vicomte de Mortemart</span>, <span class="green">Montmorencys</span>, <span class="green">Rohans</span>, <span class="green">Abbe Morio</span>, <span class="green">the Emperor</span>, <span class="red">I shall be delighted to meet them,</span>, <span class="green">the prince</span>, <span class="red">But tell me,</span>, <span class="red">is it true that the Dowager Empress wants Baron Funke
    to be appointed first secretary at Vienna? The baron by all accounts
    is a poor creature.</span>, <span class="green">Prince Vasili</span>, <span class="green">Dowager Empress Marya Fedorovna</span>, <span class="green">the baron</span>, <span class="green">Anna Pavlovna</span>, <span class="green">the Empress</span>, <span class="red">Baron Funke has been recommended to the Dowager Empress by her
    sister,</span>, <span class="green">the Empress</span>, <span class="green">Anna Pavlovna's</span>, <span class="green">Her Majesty</span>, <span class="green">Baron
    Funke</span>, <span class="green">The prince</span>, <span class="green">Anna
    Pavlovna</span>, <span class="green">the Empress</span>, <span class="red">Now about your family. Do you know that since your daughter came
    out everyone has been enraptured by her? They say she is amazingly
    beautiful.</span>, <span class="green">The prince</span>, <span class="red">I often think,</span>, <span class="red">I often think how unfairly sometimes the
    joys of life are distributed. Why has fate given you two such splendid
    children? I don't speak of <span class="green">Anatole</span>, your youngest. I don't like
    him,</span>, <span class="green">Anatole</span>, <span class="red">Two such charming children. And really you appreciate
    them less than anyone, and so you don't deserve to have them.</span>, <span class="red">I can't help it,</span>, <span class="green">the prince</span>, <span class="red">Lavater would have said I
    lack the bump of paternity.</span>, <span class="red">Don't joke; I mean to have a serious talk with you. Do you know I
    am dissatisfied with your younger son? Between ourselves</span>, <span class="red">he was mentioned at Her
    Majesty's and you were pitied....</span>, <span class="green">The prince</span>, <span class="red">What would you have me do?</span>, <span class="red">You know I did all
    a father could for their education, and they have both turned out
    fools. Hippolyte is at least a quiet fool, but Anatole is an active
    one. That is the only difference between them.</span>, <span class="red">And why are children born to such men as you? If you were not a
    father there would be nothing I could reproach you with,</span>, <span class="green">Anna
    Pavlovna</span>, <span class="red">I am your faithful slave and to you alone I can confess that my
    children are the bane of my life. It is the cross I have to bear. That
    is how I explain it to myself. It can't be helped!</span>, <span class="green">Anna Pavlovna</span>]



```python
# if you want to find the number of times “the prince” is surrounded by tags on the example page, textcontet= the prince
nameList = bs.find_all(text='the prince')
print(len(nameList))
```

    7



```python
# This returns the first tag with the word “text” in the class_ attribute and “title” in the id attribute
title = bs.find_all(id='title', class_='text')
print([text for text in title])
# these two lines are identical
bs.find_all(id='text')
bs.find_all('', {'id':'text'})
```

    []





    [<div id="text">
     "<span class="red">Well, Prince, so Genoa and Lucca are now just family estates of the
     Buonapartes. But I warn you, if you don't tell me that this means war,
     if you still try to defend the infamies and horrors perpetrated by
     that Antichrist- I really believe he is Antichrist- I will have
     nothing more to do with you and you are no longer my friend, no longer
     my 'faithful slave,' as you call yourself! But how do you do? I see
     I have frightened you- sit down and tell me all the news.</span>"
     <p></p>
     It was in July, 1805, and the speaker was the well-known <span class="green">Anna
     Pavlovna Scherer</span>, maid of honor and favorite of the <span class="green">Empress Marya
     Fedorovna</span>. With these words she greeted <span class="green">Prince Vasili Kuragin</span>, a man
     of high rank and importance, who was the first to arrive at her
     reception. <span class="green">Anna Pavlovna</span> had had a cough for some days. She was, as
     she said, suffering from la grippe; grippe being then a new word in
     <span class="green">St. Petersburg</span>, used only by the elite.
     <p></p>
     All her invitations without exception, written in French, and
     delivered by a scarlet-liveried footman that morning, ran as follows:
     <p></p>
     "<span class="red">If you have nothing better to do, Count [or Prince], and if the
     prospect of spending an evening with a poor invalid is not too
     terrible, I shall be very charmed to see you tonight between 7 and 10-
     Annette Scherer.</span>"
     <p></p>
     "<span class="red">Heavens! what a virulent attack!</span>" replied <span class="green">the prince</span>, not in the
     least disconcerted by this reception. He had just entered, wearing
     an embroidered court uniform, knee breeches, and shoes, and had
     stars on his breast and a serene expression on his flat face. He spoke
     in that refined French in which our grandfathers not only spoke but
     thought, and with the gentle, patronizing intonation natural to a
     man of importance who had grown old in society and at court. He went
     up to <span class="green">Anna Pavlovna</span>, kissed her hand, presenting to her his bald,
     scented, and shining head, and complacently seated himself on the
     sofa.
     <p></p>
     "<span class="red">First of all, dear friend, tell me how you are. Set your friend's
     mind at rest,</span>" said he without altering his tone, beneath the
     politeness and affected sympathy of which indifference and even
     irony could be discerned.
     <p></p>
     "<span class="red">Can one be well while suffering morally? Can one be calm in times
     like these if one has any feeling?</span>" said <span class="green">Anna Pavlovna</span>. "<span class="red">You are
     staying the whole evening, I hope?</span>"
     <p></p>
     "<span class="red">And the fete at the English ambassador's? Today is Wednesday. I
     must put in an appearance there,</span>" said <span class="green">the prince</span>. "<span class="red">My daughter is
     coming for me to take me there.</span>"
     <p></p>
     "<span class="red">I thought today's fete had been canceled. I confess all these
     festivities and fireworks are becoming wearisome.</span>"
     <p></p>
     "<span class="red">If they had known that you wished it, the entertainment would
     have been put off,</span>" said <span class="green">the prince</span>, who, like a wound-up clock, by
     force of habit said things he did not even wish to be believed.
     <p></p>
     "<span class="red">Don't tease! Well, and what has been decided about Novosiltsev's
     dispatch? You know everything.</span>"
     <p></p>
     "<span class="red">What can one say about it?</span>" replied <span class="green">the prince</span> in a cold,
     listless tone. "<span class="red">What has been decided? They have decided that
     Buonaparte has burnt his boats, and I believe that we are ready to
     burn ours.</span>"
     <p></p>
     <span class="green">Prince Vasili</span> always spoke languidly, like an actor repeating a
     stale part. <span class="green">Anna Pavlovna</span> Scherer on the contrary, despite her forty
     years, overflowed with animation and impulsiveness. To be an
     enthusiast had become her social vocation and, sometimes even when she
     did not feel like it, she became enthusiastic in order not to
     disappoint the expectations of those who knew her. The subdued smile
     which, though it did not suit her faded features, always played
     round her lips expressed, as in a spoiled child, a continual
     consciousness of her charming defect, which she neither wished, nor
     could, nor considered it necessary, to correct.
     <p></p>
     In the midst of a conversation on political matters <span class="green">Anna Pavlovna</span>
     burst out:
     <p></p>
     "<span class="red">Oh, don't speak to me of Austria. Perhaps I don't understand
     things, but Austria never has wished, and does not wish, for war.
     She is betraying us! Russia alone must save Europe. Our gracious
     sovereign recognizes his high vocation and will be true to it. That is
     the one thing I have faith in! Our good and wonderful sovereign has to
     perform the noblest role on earth, and he is so virtuous and noble
     that God will not forsake him. He will fulfill his vocation and
     crush the hydra of revolution, which has become more terrible than
     ever in the person of this murderer and villain! We alone must
     avenge the blood of the just one.... Whom, I ask you, can we rely
     on?... England with her commercial spirit will not and cannot
     understand the Emperor Alexander's loftiness of soul. She has
     refused to evacuate Malta. She wanted to find, and still seeks, some
     secret motive in our actions. What answer did Novosiltsev get? None.
     The English have not understood and cannot understand the
     self-abnegation of our Emperor who wants nothing for himself, but only
     desires the good of mankind. And what have they promised? Nothing! And
     what little they have promised they will not perform! Prussia has
     always declared that Buonaparte is invincible, and that all Europe
     is powerless before him.... And I don't believe a word that Hardenburg
     says, or Haugwitz either. This famous Prussian neutrality is just a
     trap. I have faith only in God and the lofty destiny of our adored
     monarch. He will save Europe!</span>"
     <p></p>
     She suddenly paused, smiling at her own impetuosity.
     <p></p>
     "<span class="red">I think,</span>" said <span class="green">the prince</span> with a smile, "<span class="red">that if you had been
     sent instead of our dear <span class="green">Wintzingerode</span> you would have captured the
     <span class="green">King of Prussia</span>'s consent by assault. You are so eloquent. Will you
     give me a cup of tea?</span>"
     <p></p>
     "<span class="red">In a moment. A propos,</span>" she added, becoming calm again, "<span class="red">I am
     expecting two very interesting men tonight, <span class="green">le Vicomte de Mortemart</span>,
     who is connected with the <span class="green">Montmorencys</span> through the <span class="green">Rohans</span>, one of
     the best French families. He is one of the genuine emigres, the good
     ones. And also the <span class="green">Abbe Morio</span>. Do you know that profound thinker? He
     has been received by <span class="green">the Emperor</span>. Had you heard?</span>"
     <p></p>
     "<span class="red">I shall be delighted to meet them,</span>" said <span class="green">the prince</span>. "<span class="red">But tell me,</span>"
     he added with studied carelessness as if it had only just occurred
     to him, though the question he was about to ask was the chief motive
     of his visit, "<span class="red">is it true that the Dowager Empress wants Baron Funke
     to be appointed first secretary at Vienna? The baron by all accounts
     is a poor creature.</span>"
     <p></p>
     <span class="green">Prince Vasili</span> wished to obtain this post for his son, but others
     were trying through the <span class="green">Dowager Empress Marya Fedorovna</span> to secure it
     for <span class="green">the baron</span>.
     <p></p>
     <span class="green">Anna Pavlovna</span> almost closed her eyes to indicate that neither she
     nor anyone else had a right to criticize what <span class="green">the Empress</span> desired or
     was pleased with.
     <p></p>
     "<span class="red">Baron Funke has been recommended to the Dowager Empress by her
     sister,</span>" was all she said, in a dry and mournful tone.
     <p></p>
     As she named <span class="green">the Empress</span>, <span class="green">Anna Pavlovna's</span> face suddenly assumed an
     expression of profound and sincere devotion and respect mingled with
     sadness, and this occurred every time she mentioned her illustrious
     patroness. She added that <span class="green">Her Majesty</span> had deigned to show <span class="green">Baron
     Funke</span>, and again her face clouded over with sadness.
     <p></p>
     <span class="green">The prince</span> was silent and looked indifferent. But, with the
     womanly and courtierlike quickness and tact habitual to her, <span class="green">Anna
     Pavlovna</span> wished both to rebuke him (for daring to speak he had done of
     a man recommended to <span class="green">the Empress</span>) and at the same time to console him,
     so she said:
     <p></p>
     "<span class="red">Now about your family. Do you know that since your daughter came
     out everyone has been enraptured by her? They say she is amazingly
     beautiful.</span>"
     <p></p>
     <span class="green">The prince</span> bowed to signify his respect and gratitude.
     <p></p>
     "<span class="red">I often think,</span>" she continued after a short pause, drawing nearer
     to the prince and smiling amiably at him as if to show that
     political and social topics were ended and the time had come for
     intimate conversation- "<span class="red">I often think how unfairly sometimes the
     joys of life are distributed. Why has fate given you two such splendid
     children? I don't speak of <span class="green">Anatole</span>, your youngest. I don't like
     him,</span>" she added in a tone admitting of no rejoinder and raising her
     eyebrows. "<span class="red">Two such charming children. And really you appreciate
     them less than anyone, and so you don't deserve to have them.</span>"
     <p></p>
     And she smiled her ecstatic smile.
     <p></p>
     "<span class="red">I can't help it,</span>" said <span class="green">the prince</span>. "<span class="red">Lavater would have said I
     lack the bump of paternity.</span>"
     <p></p>
     "<span class="red">Don't joke; I mean to have a serious talk with you. Do you know I
     am dissatisfied with your younger son? Between ourselves</span>" (and her
     face assumed its melancholy expression), "<span class="red">he was mentioned at Her
     Majesty's and you were pitied....</span>"
     <p></p>
     <span class="green">The prince</span> answered nothing, but she looked at him significantly,
     awaiting a reply. He frowned.
     <p></p>
     "<span class="red">What would you have me do?</span>" he said at last. "<span class="red">You know I did all
     a father could for their education, and they have both turned out
     fools. Hippolyte is at least a quiet fool, but Anatole is an active
     one. That is the only difference between them.</span>" He said this smiling
     in a way more natural and animated than usual, so that the wrinkles
     round his mouth very clearly revealed something unexpectedly coarse
     and unpleasant.
     <p></p>
     "<span class="red">And why are children born to such men as you? If you were not a
     father there would be nothing I could reproach you with,</span>" said <span class="green">Anna
     Pavlovna</span>, looking up pensively.
     <p></p>
     "<span class="red">I am your faithful slave and to you alone I can confess that my
     children are the bane of my life. It is the cross I have to bear. That
     is how I explain it to myself. It can't be helped!</span>"
     <p></p>
     He said no more, but expressed his resignation to cruel fate by a
     gesture. <span class="green">Anna Pavlovna</span> meditated.
     </div>]



## Difference between children and descendants


```python
# see the source code of the website to understand the structure
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
# This code prints the list of product rows in the giftList table, including the initial row of column labels.
# children are always exactly one tag below a parent, whereas descendants can be at any level in the tree below a parent.
for child in bs.find('table',{'id':'giftList'}).children:
    print(child)
```



    <tr><th>
    Item Title
    </th><th>
    Description
    </th><th>
    Cost
    </th><th>
    Image
    </th></tr>


    <tr class="gift" id="gift1"><td>
    Vegetable Basket
    </td><td>
    This vegetable basket is the perfect gift for your health conscious (or overweight) friends!
    <span class="excitingNote">Now with super-colorful bell peppers!</span>
    </td><td>
    $15.00
    </td><td>
    <img src="../img/gifts/img1.jpg"/>
    </td></tr>


    <tr class="gift" id="gift2"><td>
    Russian Nesting Dolls
    </td><td>
    Hand-painted by trained monkeys, these exquisite dolls are priceless! And by "priceless," we mean "extremely expensive"! <span class="excitingNote">8 entire dolls per set! Octuple the presents!</span>
    </td><td>
    $10,000.52
    </td><td>
    <img src="../img/gifts/img2.jpg"/>
    </td></tr>


    <tr class="gift" id="gift3"><td>
    Fish Painting
    </td><td>
    If something seems fishy about this painting, it's because it's a fish! <span class="excitingNote">Also hand-painted by trained monkeys!</span>
    </td><td>
    $10,005.00
    </td><td>
    <img src="../img/gifts/img3.jpg"/>
    </td></tr>


    <tr class="gift" id="gift4"><td>
    Dead Parrot
    </td><td>
    This is an ex-parrot! <span class="excitingNote">Or maybe he's only resting?</span>
    </td><td>
    $0.50
    </td><td>
    <img src="../img/gifts/img4.jpg"/>
    </td></tr>


    <tr class="gift" id="gift5"><td>
    Mystery Box
    </td><td>
    If you love surprises, this mystery box is for you! Do not place on light-colored surfaces. May cause oil staining. <span class="excitingNote">Keep your friends guessing!</span>
    </td><td>
    $1.50
    </td><td>
    <img src="../img/gifts/img6.jpg"/>
    </td></tr>




## Pay attention to NEXT siblings


```python
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

for sibling in bs.find('table', {'id':'giftList'}).tr.next_siblings:
    print(sibling)
```



    <tr class="gift" id="gift1"><td>
    Vegetable Basket
    </td><td>
    This vegetable basket is the perfect gift for your health conscious (or overweight) friends!
    <span class="excitingNote">Now with super-colorful bell peppers!</span>
    </td><td>
    $15.00
    </td><td>
    <img src="../img/gifts/img1.jpg"/>
    </td></tr>


    <tr class="gift" id="gift2"><td>
    Russian Nesting Dolls
    </td><td>
    Hand-painted by trained monkeys, these exquisite dolls are priceless! And by "priceless," we mean "extremely expensive"! <span class="excitingNote">8 entire dolls per set! Octuple the presents!</span>
    </td><td>
    $10,000.52
    </td><td>
    <img src="../img/gifts/img2.jpg"/>
    </td></tr>


    <tr class="gift" id="gift3"><td>
    Fish Painting
    </td><td>
    If something seems fishy about this painting, it's because it's a fish! <span class="excitingNote">Also hand-painted by trained monkeys!</span>
    </td><td>
    $10,005.00
    </td><td>
    <img src="../img/gifts/img3.jpg"/>
    </td></tr>


    <tr class="gift" id="gift4"><td>
    Dead Parrot
    </td><td>
    This is an ex-parrot! <span class="excitingNote">Or maybe he's only resting?</span>
    </td><td>
    $0.50
    </td><td>
    <img src="../img/gifts/img4.jpg"/>
    </td></tr>


    <tr class="gift" id="gift5"><td>
    Mystery Box
    </td><td>
    If you love surprises, this mystery box is for you! Do not place on light-colored surfaces. May cause oil staining. <span class="excitingNote">Keep your friends guessing!</span>
    </td><td>
    $1.50
    </td><td>
    <img src="../img/gifts/img6.jpg"/>
    </td></tr>




## Find all the image and find it's parent (td in this case)


```python
# navigate in dom tree
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
print(bs.find('img',
              {'src':'../img/gifts/img1.jpg'})
      .parent.previous_sibling.get_text())
```


    $15.00



## Use regular expressions to find all the images in the websites


```python
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
# using regular expressions
images = bs.find_all('img', {'src':re.compile('\.\.\/img\/gifts/img.*\.jpg')})
for image in images:
    print(image['src'])
# note that images is an object of beautiful soup
type(images)
```

    ../img/gifts/img1.jpg
    ../img/gifts/img2.jpg
    ../img/gifts/img3.jpg
    ../img/gifts/img4.jpg
    ../img/gifts/img6.jpg





    bs4.element.ResultSet



## Use lambda function to implement some nice functions


```python
# using anonymous functions
# it will find tags with two attributes, such as the following:
bs.find_all(lambda tag: len(tag.attrs) == 2)
```




    [<img src="../img/gifts/logo.jpg" style="float:left;"/>,
     <tr class="gift" id="gift1"><td>
     Vegetable Basket
     </td><td>
     This vegetable basket is the perfect gift for your health conscious (or overweight) friends!
     <span class="excitingNote">Now with super-colorful bell peppers!</span>
     </td><td>
     $15.00
     </td><td>
     <img src="../img/gifts/img1.jpg"/>
     </td></tr>,
     <tr class="gift" id="gift2"><td>
     Russian Nesting Dolls
     </td><td>
     Hand-painted by trained monkeys, these exquisite dolls are priceless! And by "priceless," we mean "extremely expensive"! <span class="excitingNote">8 entire dolls per set! Octuple the presents!</span>
     </td><td>
     $10,000.52
     </td><td>
     <img src="../img/gifts/img2.jpg"/>
     </td></tr>,
     <tr class="gift" id="gift3"><td>
     Fish Painting
     </td><td>
     If something seems fishy about this painting, it's because it's a fish! <span class="excitingNote">Also hand-painted by trained monkeys!</span>
     </td><td>
     $10,005.00
     </td><td>
     <img src="../img/gifts/img3.jpg"/>
     </td></tr>,
     <tr class="gift" id="gift4"><td>
     Dead Parrot
     </td><td>
     This is an ex-parrot! <span class="excitingNote">Or maybe he's only resting?</span>
     </td><td>
     $0.50
     </td><td>
     <img src="../img/gifts/img4.jpg"/>
     </td></tr>,
     <tr class="gift" id="gift5"><td>
     Mystery Box
     </td><td>
     If you love suprises, this mystery box is for you! Do not place on light-colored surfaces. May cause oil staining. <span class="excitingNote">Keep your friends guessing!</span>
     </td><td>
     $1.50
     </td><td>
     <img src="../img/gifts/img6.jpg"/>
     </td></tr>]




```python
# use of lambda functions to replace some built-in bs functions
bs.find_all(lambda tag: tag.get_text() == 'Or maybe he\'s only resting?')
bs.find_all('', text='Or maybe he\'s only resting?')
```




    ["Or maybe he's only resting?"]




```python
bs.find_all(lambda tag: tag.get_text() == 'Or maybe he\'s only resting?')
```




    [<span class="excitingNote">Or maybe he's only resting?</span>]


