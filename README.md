# ReactJS-ReduxJS-Starter-Boilerplate

Architect Enterprise ReactJS-ReduxJS-Saga-WebPack-Django-Starter-Boilerplate Web Application

#### Django Mocks as Json Server Data

#### Use Fractal Project Structure (https://github.com/davezuko/react-redux-starter-kit/wiki/Fractal-Project-Structure)

Why Architecting from day one important,
Small Apps can built with flat directory structure, like components, containers, etc.
fails to scale, fails velocity as project grows...

Large app is like large tree :evergreen_tree:,
Ex:
Trunk--> Router
Braches--> Route Bundles
Leaves--> Views (can be Common/ Shared/ Container Components)
Global app with UI --> Close to Trunk @base of hugh brach, like `/app` route

#### Use Ducks Modular Redux (https://github.com/erikras/ducks-modular-redux)

Remeber,
You wraps your whole app inside <Provider > tag, --> attribute of `store={store}`
--> which is `CreateStore({})` --> `CombineReducer({})` --> `rootReducer` with simple `reducers`

1. Composition over Inheritance (old dependency injection concept again)
   Use Functional Compoenets where ever possible
   Keep render method as small as possible
