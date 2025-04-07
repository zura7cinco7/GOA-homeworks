const getElementByIdManual = function(id) {
    const children = document.body.children;

    for (let i = 0; i < children.length; i++) {
        if (children[i].id === id) {
            return children[i];
        }
    }

    return null;
}

const getElementsByClassName = function(className) {
    const elements = [];
    const allElements = document.getElementsByTagName('*'); 

    for (let i = 0; i < allElements.length; i++) {
        if (allElements[i].classList.contains(className)) {
            elements.push(allElements[i]);
        }
    }

    return elements.length === 1 ? elements[0] : elements;
}

const getElementsByTagName = function(tagName) {
    const elements = [];
    const allElements = document.getElementsByTagName(tagName);

    for (let i = 0; i < allElements.length; i++) {
        elements.push(allElements[i]);
    }

    return elements.length === 1 ? elements[0] : elements;
}

const manualQuerySelector = function(searchQuery) {
    if (searchQuery[0] === "#") {
        return getElementByIdManual(searchQuery.slice(1));
    } else if (searchQuery[0] === ".") {
        return getElementsByClassName(searchQuery.slice(1));
    } else {
        return getElementsByTagName(searchQuery);
    }
}
