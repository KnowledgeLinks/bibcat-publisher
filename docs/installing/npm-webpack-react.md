author:  http://orcid.org/0000-0002-7543-3893
title: Installing Node.js, Webpack, and React

## Installing Node.js, Webpack, and React.js
### Step 1. Install Node.js and NPM
[Download](https://nodejs.org/en/download/) and install the
latest version of [Node.js][NODE]. This will install [NPM][NPM]
in your environment.

### Step 2. Install Webpack
[Webpack][WEBPCK] is a [Node.js][NODE] module bundler that is used in
[BIBCAT Publisher][BCPUB] to manage JavaScript, Media, and CSS dependencies.
From your command line, run the following command in the
`bibcat-publisher/catalog/static` directory.

```
cd /path/to/bibcat-publisher/catalog/static
npm install --save webpack
```
### Step 3. Install React and Babel
The user interface in [BIBCAT Publisher][BCPUB] is built using
[React.js][REACT] components.

```
npm install --save react react-dom
```

React UI components are built in a JavaScript extension called
[JSX][JSX] that requires the [Babel][BABEL] NPM package:

```
npm install --save babel-core babel-loader babel-preset-react babel-preset-env
```

### Step 4. Install JQuery
The [JQuery][JQ] Javascript library is used by [BIBCAT Publisher][BCPUB]
to communicate between the React Front-end UI and the back-end
semantic-server. To install [JQuery][JQ] from the command-line:

```
npm install --save jquery
```

### Step 5. Install Bootstrap
The default CSS/Javascript user interface used in [BIBCAT Publisher][BCPUB]
is [Bootstrap][BOOTSTRP] 4.0. To install [Bootstrap][BOOTSTRP] with [NPM][NPM],
from the command-line:

```
npm install --save popper.js
npm install --save bootstrap@4.0.0-beta.2
```

[BCPUB]: http://bibcat.org/publisher/
[BABEL]: http://babeljs.io/
[BOOTSTRP]: http://getbootstrap.com/
[JSX]: https://jsx.github.io/
[JQ]: http://jquery.com/
[NODE]: https://nodejs.org/en/
[NPM]: https://www.npmjs.com/
[REACT]: https://reactjs.org/
[WEBPCK]: https://webpack.js.org/
