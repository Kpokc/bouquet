<h1 align="center">DEV Blog</h1>
<h1 align="center"><img src="static/mockup/home.png" /></h1>

-[Live Website](https://edible-bouquets.herokuapp.com/)

-[GitHub Repository](https://github.com/Kpokc/bouquet/tree/master)
 
 ## About

This project is made for people who likes development. Who have some experience or articles to share, or who is looking how to solve some specific IT problems.
This website is made with the personal experience of site owner who likes to share his own solution or solutions he has found during the development. 
For site owner and users it is good ability to build a strong IT comunity.
It is designed to be responsive on all devices and easy to navigate for users and owner.


## Table of Contents

[User Experience (UX)](#UX)

[Features](#features)

[Design](#design)

[Technologies Used](#technologies)

[Testing](#testing)

[Deployment](#deployment)

<a name="UX"></a>
## User Experience (UX)
### User Stories

This website gives the information about different IT / development solutions posted by site owner and other users. 
Any one who is interested in IT / development and wants to share issues or share how to resolev problems then this website is perfect for him. 
This site also provides an option to create your own account and add a post.

- #### Generic User
    1. I want to easily understand the purpose and the layout of the site without additional instructions needed.
    1. I want to intuitively navigate through the site to browse the content.
    1. I want the site is responsive on all device as I usually use phone for doing all such type of stuff.
    1. I want to be able to use the website on any device so I can keep it handy.
    1. I want to use the navigation at all times and have it readily available so I can quickly navigate from one page to another.
    1. Copy link of a post.

- ####  Admin/Site Owner
    1. As a site owner I want to read all the recipe.
    1. As a site owner I want to add, edit and delete my recipe.
    1. As a site owner I can delete others recipe from mongo DB.
    1. As a site owner I want manage categories.I want to add, edit and delete the category from Mongo DB.
    1. As a site owner I want to recieve the feedback of users.
    1. Copy link of a post.
    
- #### User
    1. I want to check the posts without login or sign up on site.
    1. I want to get posts by search option.
    1. I want to contact the site owner by sending message without login or sign up.
    1. I want to request the site owner to add new category.
    1. Copy link of a post.

- #### User who wants to post recipe
    1. I want to create mypage by sign up.
    1. I want to easliy login and check mypage.
    1. I want to add new post and available to all users of site.
    1. I want to edit and delete my post or my comment.
    1. I want to pin posts to read them later.
    1. I want to like or dislike any comment.
    1. I want to like, dislike, pin any post.
    1. I want to contact the site owner.
    1. Copy link of a post.

<a name="design"></a>     
## Design
      
### Typography

-  The main font used is a Roboto Google fonts.

### Icons

- In this project, icons provided by Font Awesome and Materialize.

### Images

- #### 
    -[Images wehere taken: http://img.icons8.com/](http://img.icons8.com/)

### Defensive Design

- The user is not able to break the site by clicking on buttons.
- #### The add and edit post form:
    - The category has to be chosen.
    - The title must be provided by user.
    - The content (text) must be provided by user.

- #### The add and edit comment:
    - The content (text) must be provided by user.

- #### A post or comment can't be deleted by just one click. 
    If someone clicks on the delete button, there wil be a pop up modal with a confirmation
        if someone is sure to delete the post or comment.

### Mockups

- #### Mockups were created using https://wireframe.cc/.
    -[Wireframes PDF](https://github.com/Kpokc/bouquet/blob/master/wireframe/wireframes.pdf)
    -[Wireframes Cloud](https://wireframe.cc/pro/pp/a53120502454175)
    
<a name="features"></a>
## Features

### Existing Features

- #### Common Features Across All Pages

    - Header allows user to easily navigate across all pages
      - The header itself is positioned to always be visible (fixed to top) at the top of the screen (mobile and desktop) which allows visitors to find it quickly.
      - The brand logo is positioned on the left and is visible on all pages.
      - Navigation links is more visible when hovered over. This lets the visitor know that it is clickable.
      - Navigation links collapse in a home menu when viewed on mobile device.
      - Allows to like and dislike, pin any post. Like and dislike any comment.
      - Allows to copy link of a post.
    
    - Buttons/Links
      - All buttons are styled in the way to provide consistency across the page.
    
    - Flash messages
      - Messages displayed at the top of the page to provide the user confirmation of actions and disappear in one second.

    - Responsiveness
      - All Pages are responsive on different viewport size.

### Specific to Pages
- Home Page
    - This page has header, footer and search box, this page has also list of all posts with related images.The header has navigation bar. The image brings the user's attention and inviting the user to explore the post and copy post link.
    (If loged in/ sign up) can like, dislike, add, comment, copy link, pin post.
    On the right hand side user can get access to most liked, most commented and random post.

- Read Post Page
    - User can read post fully. Alsow can like, dislike, pin, delete post. Can copy link of the current post. Aswel as comment post, edit delete, like dislike comment.
    On the right hand side user can get access to most liked, most commented and random post.

- Contact Page
    - This page contains a form where users can give feedback and ask questions. It has another form where users can request for newsletter by simply subscribe it. 

- MyPage 
    - Using Mypage user can get access to his posts, his comments and pinned posts. Alsow like, dislike, edit, delete his posts and comments. Unpin posts.

- Search page. 
    -User retrieve all post where title and/or content has requested     word.

- Login Page 
    - This page has login form. After login user will reach home page.

- Sign Up Page
    - This page has sign up form. After login user will reach home page.

- Log out
    - This page will log user out.

### Future Features
  - Represent how mane likes or dislikes post or comment has.
  - When like, dislike, pin button clicked - implement ajax request to update related buttons color and python functions in the background.
  - Implement dynamicly preload posts depending on a mouse down scrolle.
  - Implement comlaints.

<a name="technologies"></a>
## Technologies Used

### Languages Used

  - [HTML5](https://en.wikipedia.org/wiki/HTML5)
  - [SCSS](https://en.wikipedia.org/wiki/SCSS)
  - [JavaScript](https://en.wikipedia.org/wiki/Javascript)
  - [Jquery](https://en.wikipedia.org/wiki/JQuery)
  - [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries and Programs Used

  - [Font Awesome](https://fontawesome.com/) - Font Awesome is used to add social icons for socila links.
  - [Google Fonts](https://fonts.google.com/) - Google Fonts is used to import 'Roboto'.
  - [Git](https://git-scm.com/) - Git is used to allow for tracking of any changes in the code and for the version control.
  - [GitPod](https://www.gitpod.io/) - GitPod, connected to GitHub, hosted the coding space and allowed the project to be committed to the Github repository.
  - [Github](https://github.com/) - GitHub is used to host the project files and publish the live website by using Git Pages.
  - [Heroku](https://www.heroku.com/) - Heroku is the cloud platform to deploying the app.
  - [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Flask is the web framework for the app.
  - [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) - Jinja is used for Python template.
  - [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/) - Werkzeug is used for password hashing and authentication and autohorization.
  
### Database

  - [MongoDB](https://www.mongodb.com/) - MongoDB is the fully managed cloud database service used for the project.
  - The project has seven collections in the database. All fields are string data type.The palanned database structure in MongoDB is as follows:
  <img src="https://github.com/Kpokc/bouquet/blob/master/dbschema/db_schema.png"/> (Please )

<a name="#testing"></a>
## Testing

### Functionality Testing
  - #### Navigation bar
     - The navigation bar stays at the top of the page on all screen sizes.
            - When the nav links clicks it opens the relevent page in same window with same header footer.
  - #### Links
  - All internal links is tested to make sure that all pages are correctly connected.
    
### CSS3 validator 
Validate by direct input 
    [CSS Validator](https://jigsaw.w3.org/css-validator/)
  - Test result : -webkit-box-sizing is an unknown vendor extension (validator issue)

### HTML5 validator
Vaidate by direct input 
    [HTML5 Validator](https://validator.w3.org/#validate_by_input)
  - Test result : On all pages there are only some python errors.

### JavaScript validator
Validate by direct input
    [JavaScript Validator](https://jshint.com/)
  - Test result : Errors removed (mostly ';' missing)

### Python Validator
Validate by direct input
    [Pyhton Validator](https://extendsclass.com/)
  - Test result : No syntax errors detected

### Usability Testing
  - This website is with friends to check on different device and accessbility.

### Compatibility Testing
  - #### Browser Compatibility
    - Tested on Chrome, Firefox, Opera, Microsoft Edge, Safari.
  - #### OS Compatibility
    - Tested on iOS , Android 10 and Windows 10.
  - #### Tested for responsivness on [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools). 

### Testing User Stories 
- #### Generic User
    - I easily understand the purpose and the layout of the site without additional instructions needed.
    - The main page is simple and clear with a search box and list of all posts. 
    - All pages of website has navigation bar. 
    - With navigation bar I can easily access diiferent page and go anywhere from present page and come back.
        - Home Page
            - Home page provides the search box to search the specific posts and list of all posts of site.I can like / dislike / pin / copy link of any page. Alsow edit my post.
        - Contact Page
            - Contact page provides me contact form for feedback or query.
        - Login Page
            -  In this page I login to the website and open my page.
        - Signup Page
            - In this page I create my account by filling the form and be able to post recipe.
        - My Page
            - In this page I can see all my posts / comments / pinned posts. I can also add, edit and delete my posts / comments or remove posts from pin.
        - Read Post Page    
            - In this page i can read / comment / like / dislike / pin any post or copy link to post. As well as like or dislike any other comment. Also edit my post or my comment.
        - Add Post page
            - In this page i can select category, add title and post it self.

- #### Site Owner/Admin 
    - I get all posts posted by me and others.
    - I can add new post.
    - I can edit and delete my post or comment anytime.
    - I can delete any post / comment from my website.
    - I can add new category.
    - I can edit and delete existing categories.
    - I can get feedback and queries of users by mail.

- #### User who wants to get recipe 
    - I get the list of all posts.
    - I get the specificpost by search option.
    - I can contact site owner by contact form and also can give feedback.
    - I can like / dislike / comment or copy a link of any post.
    - I can also create my account on website by sign up form.
    
- #### User who wants to post recipe
    - I can easily add post after login.
    - I can edit and delete my post / comment from website anytime. I can like or dislike any post or comment.
    - I can see all posts of website but can not edit and delete others posts.

<a name="deployment"></a>
## Deployment

- ### Working with the local copy
  1. Install all the requirements: Go to the workspace of your local copy. In the terminal window of your IDE type: pip3 install -r requirements.txt.
  2. Create a database in MongoDB
     - Signup or login to your MongoDB account.
     - Create a cluster and a database.
     - Create five collections in the db: categories, recipes, feedback, newsletter, users.
     - Add string values for the collections. See my database section how the database is set up for this project.
  3. Create the environment variables
     - Create a .gitignore file in the root directory of the project.
     - Add the env.py file in the .gitignore.
     - Create the file env.py. This will contain all the envornment variables.
        - Import os
        - os.environ.setdefault("IP", "your code")
        - os.environ.setdefault("PORT", "your code")
        - os.environ.setdefault("SECRET_KEY", "your code")
        - os.environ.setdefault("MONGO_URI", "your code")
        - os.environ.setdefault("MONGO_DBNAME", "your code")
  4. Run the app: Open your terminal window in your IDE. Type python3 app.py and run the app.
  
- ### Heroku Deployment
  1. Set up local workspace for Heroku
     - In terminal window of your IDE type: pip3 freeze -- local > requirements.txt. (The file is needed for Heroku to know which filed to install.)
     - In termial window of your IDE type: python app.py > Procfile (The file is needed for Heroku to know which file is needed as entry point.)
  2. Set up Heroku: create a Heroku account and create a new app and select your region.
  3. Deployment method 'Github'
     - Click on the Connect to GitHub section in the deploy tab in Heroku.
       - Search your repository to connect with it.
       - When your repository appears click on connect to connect your repository with the Heroku.
     - Go to the settings app in Heroku and go to Config Vars. Click on Reveal Config Vars.
       - Enter the variables contained in your env.py file. it is about: IP, PORT, SECRET_KEY, MONGO_URI, MONGO_DBNAME
  4. Push the requirements.txt and Procfile to repository.
     - $ git add requirements.txt
     - $ git commit -m "Add requirements.txt"
     - $ git add Procfile 
     - $ git commit -m "Add Procfile"
  5. Automatic deployment: Go to the deploy tab in Heroku and scroll down to Aotmatic deployments. Click on Enable Automatic Deploys. By Manual deploy click on Deploy Branch.

  Heroku will receive the code from Github and host the app using the required packages. Click on Open app in the right corner of your Heroku account. The app wil open and the live link is available from the address bar. 

- ### Forking
  If you wish to contribute to this website you can Fork it without affecting the main branch by following the procedure outlined below.
  1. Go to the GitHub website and log in.
  2. Locate the [Repository](https://github.com/Kpokc/bouquet/tree/master) used for this project.
  3. On the right-hand side of the Repository name, you'll see the 'Fork' button. It's located next to the 'Star' and 'Watch' buttons.
  4. This will create a copy in your personal repository.
  5. Once you're finished making changes you can locate the 'New Pull Request' button just above the file listing in the original repository.

- ### Cloning 
  If you wish to clone or download this repository to your local device you can follow the procedure outlined below.
  1. Go to the GitHub website and log in.
  2. Locate the [Repository](https://github.com/Kpokc/bouquet/tree/master) used for this project.
  3. Under the Repository name locate 'Clone or Download' button in green.
  4. To clone the repository using HTTPS click the link under "Clone with HTTPS".
  5. Open your Terminal and go to a directory where you want the cloned directory to be copied in.
  6. Type `Git Clone` and paste the URL you copied from the GitHub.
  7. To create your local clone press `Enter`

### Code :

- materializecss library was used to create a responsive design. 
 
### Content :

- All code was written by the Ruby Srivastava.

- To write up a README file the most helpful documents were
    - Code Institute [SampleREADME](https://github.com/Code-Institute-Solutions/SampleREADME)
    - Code Institute [README Template](https://github.com/Code-Institute-Solutions/readme-template)
    

### Media :
- Icons 
        - [fontawesome.com](https://fontawesome.com/)
        - [materializecss.com](https://materializecss.com/icons.html)
- Images
        - [img.icons8.com](https://img.icons8.com/)

### Acknowledgements :

- Thanks to my fellow student and tutors on slack channel who helped me in some way.
- Thanks to my mentor Maranatha Ilesalnmi for helping me throughout the project and giving me important suggestions and feedback of my work.
 
