Information

This package is for registering public global templates in an easy way.

- Add the zcml registration stuff to your configure zcml.
- Create a folder.
- Put files in with ending .pt
- Enjoy your saved time

Minimum zcml config example


    <configure xmlns="http://namespaces.zope.org/zope"
       xmlns:browser="http://namespaces.zope.org/browser"
       xmlns:five="http://namespaces.zope.org/five"
       xmlns:pt="http://namespaces.plone.org/pt">
    
        <pt:registry
            path="templates"/>
    
    </configure>
