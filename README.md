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

1. `<Route path="" component="">` --> inside `<Switch>` --> renders first matched component
2. `<Route component="">` NO path attribute --> Error Handling when no path gets Matched

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

1. .happypack
2. dist --> build minimised code gets created here, after `npm build`
3. node_modules --> `npm i` or `yarn install`
4. server
5. src

   1. components
      use readymade files here directly
   2. containers
      Makes use of .propTypes and .defaultTypes for Clean code with Linting Errors like TypeScipt compile time errors....
      Lint will act upon while passing unvalidated props
      1. App
         1. App.js
            export class AppComponent extends Component{}
            const mapStateToProps = (state) => ({});
            AppComponent.propTypes = {};
            export const App = connect(mapStateToProps, {})(HOCsComponentHere(AppComponent, NotFoundImportedFromComponent));
         2. App.module.scss
            styling
      2. AppContainer
         export function AppContainerComponent(props) {}
         export const AppContainer = connect(mapStateToProps)(AppContainerComponent);

index.js----> just export all above components, thats all
export { App } from './App/App';

3.  HOCS
4.  images
5.  lib
6.  modules
7.  routes
8.  store
9.  styles
10. utils
11. vendors
    index.js
    reducers.js
    sagas.js

12. webpack

#### Component vs PureComponent vs Stateless Functional Component

##### when to move your code into a component, ask yourself:

i) Is your code’s functionality becoming unwieldy?
ii) Does it represent its own thing?
iii) Are you going to reuse your code?

##### If any of these question’s answer is yes, then you need to move your code into a component.

      Makes use of .propTypes and .defaultTypes for Clean code with Linting Errors like TypeScipt compile time errors....
      Lint will act upon while passing unvalidated props,
      Here assume, `userIsLoaded` is not required, so, added false in `defaultProps`,
      If it is required, then we don’t have to define a default prop for it.

##### Pure Component

export default class Profile extends PureComponent {

   static propTypes = {
   userIsLoaded: PropTypes.bool,
   user: PropTypes.shape({\_id: PropTypes.string,}).isRequired,
   }

   static defaultProps = {
   userIsLoaded: false,
   }

   render() {
      <Compo1 />
      <Compo2 />
      <Compo3 />
      <Compo4 />
   }

}// pure component

##### Stateless Functional Component

components that are not using any kind of state, refs, or lifecycle methods.
you are defining your component as a constant function that returns some data.
In simple words, stateless functional components are just functions that return JSX.

const Billboard = () => (
      <ZoneBlack>
      <Heading>React</Heading>
      <div className="billboard_product">
      <Link className="billboard_product-image" to="/">
      <img alt="#" src="#">
      </Link>
      <div className="billboard_product-details">
      <h3 className="sub">React</h3>
      <p>Lorem Ipsum</p>
      </div>
      </div>
      </ZoneBlack>
);

# coming....

Build Enterprise ReactJS-ReduxJS-Saga-WebPack-Django-Starter-Boilerplate Web Application
