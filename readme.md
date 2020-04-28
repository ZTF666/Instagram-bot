# 🤖Z-foll

A small python bot/ set of scripts that automates the process of login in to IG via facebook .
Send follow requests from the suggestions tab .
Unfollow people .
Download pictures from a given public profile

## THIS IS A WiP !!!!!!!!

```
Since this is still experimental , things my change or be super buggy .
Once fully finished , this section will be deleted , Until then , enjoy this lol.
```

## How to use

- **Install**

```python
pip install selenium
```

- **Download**

```
Get your chrome driver from this website :
```

👉 [ChromeDriver](http://chromedriver.chromium.org/) 👈

```

If you're using windows , you may want to put the .exe in the same folder as the script.

If you're using macOs , just move it to /usr/local/bin

I haven't tested it on linux, but i bet it's the same as macOs ...

```

## Functionalities

```
Functionalities implemented so far :

LOGIN ✔️
FOllOW ✔️
UNFOLLOW ✔️
DOWNLOAD POSTS ✔️
UNFOLLOWERS ❌

```

**Follow**
How it works & possible optimisation :

<details>
  
  <p>The logic i used is :</p>
  <p>The script opens up the 'ALL SUGGESTIONS TAB' then loads few of those suggestions</p>
  <p>Then goes through the first 30 accounts and follows them.</p>
  <p>Once it's done , it refreshes the page then repeat.</p>
  <p>It won't stop until you stop the script .</p>

  <p>You can optimise this by changing the number , i think a full page loaded displays up to 140 profiles.</p>

```python
if(x == 30):
              self.driver.refresh()
              ZTF.follow(self)
```

</details>

**Unfollow**
How it works & possible optimisation :

<details>
  
  <p>Basicaly just like the follow part</p>
  <p>I only unfollow 11 at a time , for some reason, if higher it results in a crash.</P>
  <p>You can optimise this by changing the number.</p>
  <p>BUT you need to figure out a way to scroll through everything</p>

```python
 if(K == 11):
      closemod = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button')
      closemod.click()
      ZTF.mylist(self)
```

</details>

**Download Posts (pics only)**

```
Given a profile , the script will acces it , load up the first 32 posts , get their links .
Then download the pictures .
There's a margin of error here , since some posts disapear from the code when they leave the view.
That's why i'm only able to grab the 32 first ones.
```


**Credentials**

```
As any other file containing sensitive data, credentials.py contains :
```

```python
login = 'PHONE_EMAIL_OR_USERNAME'
pwd = 'PASSWORD'
profile ='elonmusk'
```
```
Make sure to change that .
```

## LIMITATIONS :

```
The script bugs out from time to time depending on your internet speed .
The quality is shit , i made this while learning so excuse my n00bish mistakes .

The function SLEEP() , has high intervals because of my 3rd world internet , 💛 4mbps 💛 .
You should adapt it to your needs .
```

## Support

```
Any help improving this and adding more stuff is welcome ! .
```

## Contact me

```
you can contact me at ZTF666@protonmail.ch or via my portfolio
```

<div align="center">

<table>
  <tr>
    <td align="center"><a href="https://ztfportfolio.web.app/"><img src="https://avatars1.githubusercontent.com/u/32502988?v=4" width="100px;" alt=""/><br /><sub><b>ZTF666</b></sub></a><br /><a href="https://github.com/ZTF666/Twitter-bot" title="Code">💻</a> </td>
  </tr>
</table>

</div>

## License

**🤖Z-foll** released under the [MIT](LICENSE) License.

```
Made with 💘 by a 👨‍💻 on a 💻 | 2020 | ZTF666
```
