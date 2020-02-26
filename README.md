# ReactJS-ReduxJS-Starter-Boilerplate

Architect Enterprise ReactJS-ReduxJS-Saga-WebPack-Django-Starter-Boilerplate Web Application

#### Django Mocks as Json Server Data

#### Use Fractal Project Structure (https://github.com/davezuko/react-redux-starter-kit/wiki/Fractal-Project-Structure)

AKA : Self-Contained Apps, Recursive Route Hierarchy, Providers, etc

Why Architecting from day one important,
Small Apps can built with flat directory structure, like components, containers, etc.
fails to scale, fails velocity as project grows...

Large app is like large tree :evergreen_tree:,
Ex:
Trunk--> Router
Braches--> Route Bundles
Leaves--> Views (can be Common/ Shared/ Container Components)
Global app with UI --> Close to Trunk @base of hugh brach, like `/app` route

I) Routes
1. <Route path="" component=""> --> inside <Switch> --> renders first matched component
2. <Route component=""> NO path attribute --> Error Handling when no path gets Matched

    Each Route have -->
        Container Folder
        Component Folder
        Modules file (reducers, actions)
        Sagas file
        Own index file --> to define the route

3. Dont let sub router load until parent route has been loaded
    load components async then reducers sagas will be injected and available to store
    then HOCs initiates api calls for the route
This makes code-splitting possible with small .js files, loaded on demand    

II) Store

III) Layouts
    Stateless components to composed react-router components into view

IV) Components
    Reusable
    Functional stateless

V) Containers
    have data with them
    connect presentational components to actions/state (NO JSX in container components)



#### Use Ducks Modular Redux (https://github.com/erikras/ducks-modular-redux)

Remeber,
You wraps your whole app inside <Provider > tag, --> attribute of `store={store}`
--> which is `CreateStore({})` --> `CombineReducer({})` --> `rootReducer` with simple `reducers`

1. Composition over Inheritance (old dependency injection concept again)
   Use Functional Compoenets where ever possible
   Keep render method as small as possible
   Put render into different components or Things get crazyyy A SIMPLE Component with One render is FINE.

Remeber,
ReactJS Doesnt Support Inheritance --> HOCs are way to do so.....


#### Webpack for ReactJS App

"scripts": {
  "build": "webpack --mode production"
}

"scripts": {
  "start": "webpack-dev-server --open --mode development",
  "build": "webpack --mode production"
}

Using HappyPack (https://github.com/amireh/happypack)
npm install --save-dev happypack




module.exports = webpackConfig;

webpackConfig.module = {}
webpackConfig.plugins = {}


#### Component Material
https://ant.design/



#### Directory Stucture
coming....
