!function(){try{var t="undefined"!=typeof window?window:"undefined"!=typeof global?global:"undefined"!=typeof self?self:{},e=(new t.Error).stack;e&&(t._sentryDebugIds=t._sentryDebugIds||{},t._sentryDebugIds[e]="8e9ab21b-897e-4d3c-aca7-b2d4a667a40f",t._sentryDebugIdIdentifier="sentry-dbid-8e9ab21b-897e-4d3c-aca7-b2d4a667a40f")}catch(t){}}();"use strict";(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[6070],{6070:function(t,e,n){n.d(e,{x7:function(){return K},X5:function(){return V},Me:function(){return T},oo:function(){return J},US:function(){return A},RR:function(){return O},Cp:function(){return P},Qo:function(){return W},dr:function(){return z},cv:function(){return D},Jv:function(){return L},uY:function(){return E},dp:function(){return C}});var r=n(4029);function i(t,e,n){let i,{reference:o,floating:l}=t,u=(0,r.Qq)(e),f=(0,r.Wh)(e),c=(0,r.I4)(f),a=(0,r.k3)(e),s="y"===u,d=o.x+o.width/2-l.width/2,h=o.y+o.height/2-l.height/2,p=o[c]/2-l[c]/2;switch(a){case"top":i={x:d,y:o.y-l.height};break;case"bottom":i={x:d,y:o.y+o.height};break;case"right":i={x:o.x+o.width,y:h};break;case"left":i={x:o.x-l.width,y:h};break;default:i={x:o.x,y:o.y}}switch((0,r.hp)(e)){case"start":i[f]-=p*(n&&s?-1:1);break;case"end":i[f]+=p*(n&&s?-1:1)}return i}let o=async(t,e,n)=>{let{placement:r="bottom",strategy:o="absolute",middleware:l=[],platform:u}=n,f=l.filter(Boolean),c=await (null==u.isRTL?void 0:u.isRTL(e)),a=await u.getElementRects({reference:t,floating:e,strategy:o}),{x:s,y:d}=i(a,r,c),h=r,p={},g=0;for(let n=0;n<f.length;n++){let{name:l,fn:m}=f[n],{x:w,y:y,data:x,reset:v}=await m({x:s,y:d,initialPlacement:r,placement:h,strategy:o,middlewareData:p,rects:a,platform:u,elements:{reference:t,floating:e}});s=null!=w?w:s,d=null!=y?y:d,p={...p,[l]:{...p[l],...x}},v&&g<=50&&(g++,"object"==typeof v&&(v.placement&&(h=v.placement),v.rects&&(a=!0===v.rects?await u.getElementRects({reference:t,floating:e,strategy:o}):v.rects),{x:s,y:d}=i(a,h,c)),n=-1)}return{x:s,y:d,placement:h,strategy:o,middlewareData:p}};async function l(t,e){var n;void 0===e&&(e={});let{x:i,y:o,platform:l,rects:u,elements:f,strategy:c}=t,{boundary:a="clippingAncestors",rootBoundary:s="viewport",elementContext:d="floating",altBoundary:h=!1,padding:p=0}=(0,r.ku)(e,t),g=(0,r.yd)(p),m=f[h?"floating"===d?"reference":"floating":d],w=(0,r.JB)(await l.getClippingRect({element:null==(n=await (null==l.isElement?void 0:l.isElement(m)))||n?m:m.contextElement||await (null==l.getDocumentElement?void 0:l.getDocumentElement(f.floating)),boundary:a,rootBoundary:s,strategy:c})),y="floating"===d?{x:i,y:o,width:u.floating.width,height:u.floating.height}:u.reference,x=await (null==l.getOffsetParent?void 0:l.getOffsetParent(f.floating)),v=await (null==l.isElement?void 0:l.isElement(x))&&await (null==l.getScale?void 0:l.getScale(x))||{x:1,y:1},b=(0,r.JB)(l.convertOffsetParentRelativeRectToViewportRelativeRect?await l.convertOffsetParentRelativeRectToViewportRelativeRect({elements:f,rect:y,offsetParent:x,strategy:c}):y);return{top:(w.top-b.top+g.top)/v.y,bottom:(b.bottom-w.bottom+g.bottom)/v.y,left:(w.left-b.left+g.left)/v.x,right:(b.right-w.right+g.right)/v.x}}function u(t,e){return{top:t.top-e.height,right:t.right-e.width,bottom:t.bottom-e.height,left:t.left-e.width}}function f(t){return r.mA.some(e=>t[e]>=0)}function c(t){let e=(0,r.VV)(...t.map(t=>t.left)),n=(0,r.VV)(...t.map(t=>t.top));return{x:e,y:n,width:(0,r.Fp)(...t.map(t=>t.right))-e,height:(0,r.Fp)(...t.map(t=>t.bottom))-n}}async function a(t,e){let{placement:n,platform:i,elements:o}=t,l=await (null==i.isRTL?void 0:i.isRTL(o.floating)),u=(0,r.k3)(n),f=(0,r.hp)(n),c="y"===(0,r.Qq)(n),a=["left","top"].includes(u)?-1:1,s=l&&c?-1:1,d=(0,r.ku)(e,t),{mainAxis:h,crossAxis:p,alignmentAxis:g}="number"==typeof d?{mainAxis:d,crossAxis:0,alignmentAxis:null}:{mainAxis:d.mainAxis||0,crossAxis:d.crossAxis||0,alignmentAxis:d.alignmentAxis};return f&&"number"==typeof g&&(p="end"===f?-1*g:g),c?{x:p*s,y:h*a}:{x:h*a,y:p*s}}var s=n(10712);function d(t){let e=(0,s.Dx)(t),n=parseFloat(e.width)||0,i=parseFloat(e.height)||0,o=(0,s.Re)(t),l=o?t.offsetWidth:n,u=o?t.offsetHeight:i,f=(0,r.NM)(n)!==l||(0,r.NM)(i)!==u;return f&&(n=l,i=u),{width:n,height:i,$:f}}function h(t){return(0,s.kK)(t)?t:t.contextElement}function p(t){let e=h(t);if(!(0,s.Re)(e))return(0,r.ze)(1);let n=e.getBoundingClientRect(),{width:i,height:o,$:l}=d(e),u=(l?(0,r.NM)(n.width):n.width)/i,f=(l?(0,r.NM)(n.height):n.height)/o;return u&&Number.isFinite(u)||(u=1),f&&Number.isFinite(f)||(f=1),{x:u,y:f}}let g=(0,r.ze)(0);function m(t){let e=(0,s.Jj)(t);return(0,s.Pf)()&&e.visualViewport?{x:e.visualViewport.offsetLeft,y:e.visualViewport.offsetTop}:g}function w(t,e,n,i){var o;void 0===e&&(e=!1),void 0===n&&(n=!1);let l=t.getBoundingClientRect(),u=h(t),f=(0,r.ze)(1);e&&(i?(0,s.kK)(i)&&(f=p(i)):f=p(t));let c=(void 0===(o=n)&&(o=!1),i&&(!o||i===(0,s.Jj)(u))&&o)?m(u):(0,r.ze)(0),a=(l.left+c.x)/f.x,d=(l.top+c.y)/f.y,g=l.width/f.x,w=l.height/f.y;if(u){let t=(0,s.Jj)(u),e=i&&(0,s.kK)(i)?(0,s.Jj)(i):i,n=t,r=(0,s.wK)(n);for(;r&&i&&e!==n;){let t=p(r),e=r.getBoundingClientRect(),i=(0,s.Dx)(r),o=e.left+(r.clientLeft+parseFloat(i.paddingLeft))*t.x,l=e.top+(r.clientTop+parseFloat(i.paddingTop))*t.y;a*=t.x,d*=t.y,g*=t.x,w*=t.y,a+=o,d+=l,n=(0,s.Jj)(r),r=(0,s.wK)(n)}}return(0,r.JB)({width:g,height:w,x:a,y:d})}function y(t,e){let n=(0,s.Lw)(t).scrollLeft;return e?e.left+n:w((0,s.tF)(t)).left+n}function x(t,e,n){void 0===n&&(n=!1);let r=t.getBoundingClientRect();return{x:r.left+e.scrollLeft-(n?0:y(t,r)),y:r.top+e.scrollTop}}function v(t,e,n){let i;if("viewport"===e)i=function(t,e){let n=(0,s.Jj)(t),r=(0,s.tF)(t),i=n.visualViewport,o=r.clientWidth,l=r.clientHeight,u=0,f=0;if(i){o=i.width,l=i.height;let t=(0,s.Pf)();(!t||t&&"fixed"===e)&&(u=i.offsetLeft,f=i.offsetTop)}return{width:o,height:l,x:u,y:f}}(t,n);else if("document"===e)i=function(t){let e=(0,s.tF)(t),n=(0,s.Lw)(t),i=t.ownerDocument.body,o=(0,r.Fp)(e.scrollWidth,e.clientWidth,i.scrollWidth,i.clientWidth),l=(0,r.Fp)(e.scrollHeight,e.clientHeight,i.scrollHeight,i.clientHeight),u=-n.scrollLeft+y(t),f=-n.scrollTop;return"rtl"===(0,s.Dx)(i).direction&&(u+=(0,r.Fp)(e.clientWidth,i.clientWidth)-o),{width:o,height:l,x:u,y:f}}((0,s.tF)(t));else if((0,s.kK)(e))i=function(t,e){let n=w(t,!0,"fixed"===e),i=n.top+t.clientTop,o=n.left+t.clientLeft,l=(0,s.Re)(t)?p(t):(0,r.ze)(1),u=t.clientWidth*l.x;return{width:u,height:t.clientHeight*l.y,x:o*l.x,y:i*l.y}}(e,n);else{let n=m(t);i={x:e.x-n.x,y:e.y-n.y,width:e.width,height:e.height}}return(0,r.JB)(i)}function b(t){return"static"===(0,s.Dx)(t).position}function R(t,e){if(!(0,s.Re)(t)||"fixed"===(0,s.Dx)(t).position)return null;if(e)return e(t);let n=t.offsetParent;return(0,s.tF)(t)===n&&(n=n.ownerDocument.body),n}function k(t,e){let n=(0,s.Jj)(t);if((0,s.tR)(t))return n;if(!(0,s.Re)(t)){let e=(0,s.Ow)(t);for(;e&&!(0,s.Py)(e);){if((0,s.kK)(e)&&!b(e))return e;e=(0,s.Ow)(e)}return n}let r=R(t,e);for(;r&&(0,s.Ze)(r)&&b(r);)r=R(r,e);return r&&(0,s.Py)(r)&&b(r)&&!(0,s.hT)(r)?n:r||(0,s.gQ)(t)||n}let F=async function(t){let e=this.getOffsetParent||k,n=this.getDimensions,i=await n(t.floating);return{reference:function(t,e,n){let i=(0,s.Re)(e),o=(0,s.tF)(e),l="fixed"===n,u=w(t,!0,l,e),f={scrollLeft:0,scrollTop:0},c=(0,r.ze)(0);if(i||!i&&!l){if(("body"!==(0,s.wk)(e)||(0,s.ao)(o))&&(f=(0,s.Lw)(e)),i){let t=w(e,!0,l,e);c.x=t.x+e.clientLeft,c.y=t.y+e.clientTop}else o&&(c.x=y(o))}let a=!o||i||l?(0,r.ze)(0):x(o,f);return{x:u.left+f.scrollLeft-c.x-a.x,y:u.top+f.scrollTop-c.y-a.y,width:u.width,height:u.height}}(t.reference,await e(t.floating),t.strategy),floating:{x:0,y:0,width:i.width,height:i.height}}},L={convertOffsetParentRelativeRectToViewportRelativeRect:function(t){let{elements:e,rect:n,offsetParent:i,strategy:o}=t,l="fixed"===o,u=(0,s.tF)(i),f=!!e&&(0,s.tR)(e.floating);if(i===u||f&&l)return n;let c={scrollLeft:0,scrollTop:0},a=(0,r.ze)(1),d=(0,r.ze)(0),h=(0,s.Re)(i);if((h||!h&&!l)&&(("body"!==(0,s.wk)(i)||(0,s.ao)(u))&&(c=(0,s.Lw)(i)),(0,s.Re)(i))){let t=w(i);a=p(i),d.x=t.x+i.clientLeft,d.y=t.y+i.clientTop}let g=!u||h||l?(0,r.ze)(0):x(u,c,!0);return{width:n.width*a.x,height:n.height*a.y,x:n.x*a.x-c.scrollLeft*a.x+d.x+g.x,y:n.y*a.y-c.scrollTop*a.y+d.y+g.y}},getDocumentElement:s.tF,getClippingRect:function(t){let{element:e,boundary:n,rootBoundary:i,strategy:o}=t,l=[..."clippingAncestors"===n?(0,s.tR)(e)?[]:function(t,e){let n=e.get(t);if(n)return n;let r=(0,s.Kx)(t,[],!1).filter(t=>(0,s.kK)(t)&&"body"!==(0,s.wk)(t)),i=null,o="fixed"===(0,s.Dx)(t).position,l=o?(0,s.Ow)(t):t;for(;(0,s.kK)(l)&&!(0,s.Py)(l);){let e=(0,s.Dx)(l),n=(0,s.hT)(l);n||"fixed"!==e.position||(i=null),(o?!n&&!i:!n&&"static"===e.position&&!!i&&["absolute","fixed"].includes(i.position)||(0,s.ao)(l)&&!n&&function t(e,n){let r=(0,s.Ow)(e);return!(r===n||!(0,s.kK)(r)||(0,s.Py)(r))&&("fixed"===(0,s.Dx)(r).position||t(r,n))}(t,l))?r=r.filter(t=>t!==l):i=e,l=(0,s.Ow)(l)}return e.set(t,r),r}(e,this._c):[].concat(n),i],u=l[0],f=l.reduce((t,n)=>{let i=v(e,n,o);return t.top=(0,r.Fp)(i.top,t.top),t.right=(0,r.VV)(i.right,t.right),t.bottom=(0,r.VV)(i.bottom,t.bottom),t.left=(0,r.Fp)(i.left,t.left),t},v(e,u,o));return{width:f.right-f.left,height:f.bottom-f.top,x:f.left,y:f.top}},getOffsetParent:k,getElementRects:F,getClientRects:function(t){return Array.from(t.getClientRects())},getDimensions:function(t){let{width:e,height:n}=d(t);return{width:e,height:n}},getScale:p,isElement:s.kK,isRTL:function(t){return"rtl"===(0,s.Dx)(t).direction}};function T(t,e,n,i){let o;void 0===i&&(i={});let{ancestorScroll:l=!0,ancestorResize:u=!0,elementResize:f="function"==typeof ResizeObserver,layoutShift:c="function"==typeof IntersectionObserver,animationFrame:a=!1}=i,d=h(t),p=l||u?[...d?(0,s.Kx)(d):[],...(0,s.Kx)(e)]:[];p.forEach(t=>{l&&t.addEventListener("scroll",n,{passive:!0}),u&&t.addEventListener("resize",n)});let g=d&&c?function(t,e){let n,i=null,o=(0,s.tF)(t);function l(){var t;clearTimeout(n),null==(t=i)||t.disconnect(),i=null}return!function u(f,c){void 0===f&&(f=!1),void 0===c&&(c=1),l();let{left:a,top:s,width:d,height:h}=t.getBoundingClientRect();if(f||e(),!d||!h)return;let p=(0,r.GW)(s),g=(0,r.GW)(o.clientWidth-(a+d)),m={rootMargin:-p+"px "+-g+"px "+-(0,r.GW)(o.clientHeight-(s+h))+"px "+-(0,r.GW)(a)+"px",threshold:(0,r.Fp)(0,(0,r.VV)(1,c))||1},w=!0;function y(t){let e=t[0].intersectionRatio;if(e!==c){if(!w)return u();e?u(!1,e):n=setTimeout(()=>{u(!1,1e-7)},1e3)}w=!1}try{i=new IntersectionObserver(y,{...m,root:o.ownerDocument})}catch(t){i=new IntersectionObserver(y,m)}i.observe(t)}(!0),l}(d,n):null,m=-1,y=null;f&&(y=new ResizeObserver(t=>{let[r]=t;r&&r.target===d&&y&&(y.unobserve(e),cancelAnimationFrame(m),m=requestAnimationFrame(()=>{var t;null==(t=y)||t.observe(e)})),n()}),d&&!a&&y.observe(d),y.observe(e));let x=a?w(t):null;return a&&function e(){let r=w(t);x&&(r.x!==x.x||r.y!==x.y||r.width!==x.width||r.height!==x.height)&&n(),x=r,o=requestAnimationFrame(e)}(),n(),()=>{var t;p.forEach(t=>{l&&t.removeEventListener("scroll",n),u&&t.removeEventListener("resize",n)}),null==g||g(),null==(t=y)||t.disconnect(),y=null,a&&cancelAnimationFrame(o)}}let A=l,D=function(t){return void 0===t&&(t=0),{name:"offset",options:t,async fn(e){var n,r;let{x:i,y:o,placement:l,middlewareData:u}=e,f=await a(e,t);return l===(null==(n=u.offset)?void 0:n.placement)&&null!=(r=u.arrow)&&r.alignmentOffset?{}:{x:i+f.x,y:o+f.y,data:{...f,placement:l}}}}},V=function(t){return void 0===t&&(t={}),{name:"autoPlacement",options:t,async fn(e){var n,i,o,u;let{rects:f,middlewareData:c,placement:a,platform:s,elements:d}=e,{crossAxis:h=!1,alignment:p,allowedPlacements:g=r.Ct,autoAlignment:m=!0,...w}=(0,r.ku)(t,e),y=void 0!==p||g===r.Ct?((u=p||null)?[...g.filter(t=>(0,r.hp)(t)===u),...g.filter(t=>(0,r.hp)(t)!==u)]:g.filter(t=>(0,r.k3)(t)===t)).filter(t=>!u||(0,r.hp)(t)===u||!!m&&(0,r.Go)(t)!==t):g,x=await l(e,w),v=(null==(n=c.autoPlacement)?void 0:n.index)||0,b=y[v];if(null==b)return{};let R=(0,r.i8)(b,f,await (null==s.isRTL?void 0:s.isRTL(d.floating)));if(a!==b)return{reset:{placement:y[0]}};let k=[x[(0,r.k3)(b)],x[R[0]],x[R[1]]],F=[...(null==(i=c.autoPlacement)?void 0:i.overflows)||[],{placement:b,overflows:k}],L=y[v+1];if(L)return{data:{index:v+1,overflows:F},reset:{placement:L}};let T=F.map(t=>{let e=(0,r.hp)(t.placement);return[t.placement,e&&h?t.overflows.slice(0,2).reduce((t,e)=>t+e,0):t.overflows[0],t.overflows]}).sort((t,e)=>t[1]-e[1]),A=(null==(o=T.filter(t=>t[2].slice(0,(0,r.hp)(t[0])?2:3).every(t=>t<=0))[0])?void 0:o[0])||T[0][0];return A!==a?{data:{index:v+1,overflows:F},reset:{placement:A}}:{}}}},E=function(t){return void 0===t&&(t={}),{name:"shift",options:t,async fn(e){let{x:n,y:i,placement:o}=e,{mainAxis:u=!0,crossAxis:f=!1,limiter:c={fn:t=>{let{x:e,y:n}=t;return{x:e,y:n}}},...a}=(0,r.ku)(t,e),s={x:n,y:i},d=await l(e,a),h=(0,r.Qq)((0,r.k3)(o)),p=(0,r.Rn)(h),g=s[p],m=s[h];if(u){let t="y"===p?"top":"left",e="y"===p?"bottom":"right",n=g+d[t],i=g-d[e];g=(0,r.uZ)(n,g,i)}if(f){let t="y"===h?"top":"left",e="y"===h?"bottom":"right",n=m+d[t],i=m-d[e];m=(0,r.uZ)(n,m,i)}let w=c.fn({...e,[p]:g,[h]:m});return{...w,data:{x:w.x-n,y:w.y-i,enabled:{[p]:u,[h]:f}}}}}},O=function(t){return void 0===t&&(t={}),{name:"flip",options:t,async fn(e){var n,i,o,u,f;let{placement:c,middlewareData:a,rects:s,initialPlacement:d,platform:h,elements:p}=e,{mainAxis:g=!0,crossAxis:m=!0,fallbackPlacements:w,fallbackStrategy:y="bestFit",fallbackAxisSideDirection:x="none",flipAlignment:v=!0,...b}=(0,r.ku)(t,e);if(null!=(n=a.arrow)&&n.alignmentOffset)return{};let R=(0,r.k3)(c),k=(0,r.Qq)(d),F=(0,r.k3)(d)===d,L=await (null==h.isRTL?void 0:h.isRTL(p.floating)),T=w||(F||!v?[(0,r.pw)(d)]:(0,r.gy)(d)),A="none"!==x;!w&&A&&T.push(...(0,r.KX)(d,v,x,L));let D=[d,...T],V=await l(e,b),E=[],O=(null==(i=a.flip)?void 0:i.overflows)||[];if(g&&E.push(V[R]),m){let t=(0,r.i8)(c,s,L);E.push(V[t[0]],V[t[1]])}if(O=[...O,{placement:c,overflows:E}],!E.every(t=>t<=0)){let t=((null==(o=a.flip)?void 0:o.index)||0)+1,e=D[t];if(e)return{data:{index:t,overflows:O},reset:{placement:e}};let n=null==(u=O.filter(t=>t.overflows[0]<=0).sort((t,e)=>t.overflows[1]-e.overflows[1])[0])?void 0:u.placement;if(!n)switch(y){case"bestFit":{let t=null==(f=O.filter(t=>{if(A){let e=(0,r.Qq)(t.placement);return e===k||"y"===e}return!0}).map(t=>[t.placement,t.overflows.filter(t=>t>0).reduce((t,e)=>t+e,0)]).sort((t,e)=>t[1]-e[1])[0])?void 0:f[0];t&&(n=t);break}case"initialPlacement":n=d}if(c!==n)return{reset:{placement:n}}}return{}}}},C=function(t){return void 0===t&&(t={}),{name:"size",options:t,async fn(e){var n,i;let o,u;let{placement:f,rects:c,platform:a,elements:s}=e,{apply:d=()=>{},...h}=(0,r.ku)(t,e),p=await l(e,h),g=(0,r.k3)(f),m=(0,r.hp)(f),w="y"===(0,r.Qq)(f),{width:y,height:x}=c.floating;"top"===g||"bottom"===g?(o=g,u=m===(await (null==a.isRTL?void 0:a.isRTL(s.floating))?"start":"end")?"left":"right"):(u=g,o="end"===m?"top":"bottom");let v=x-p.top-p.bottom,b=y-p.left-p.right,R=(0,r.VV)(x-p[o],v),k=(0,r.VV)(y-p[u],b),F=!e.middlewareData.shift,L=R,T=k;if(null!=(n=e.middlewareData.shift)&&n.enabled.x&&(T=b),null!=(i=e.middlewareData.shift)&&i.enabled.y&&(L=v),F&&!m){let t=(0,r.Fp)(p.left,0),e=(0,r.Fp)(p.right,0),n=(0,r.Fp)(p.top,0),i=(0,r.Fp)(p.bottom,0);w?T=y-2*(0!==t||0!==e?t+e:(0,r.Fp)(p.left,p.right)):L=x-2*(0!==n||0!==i?n+i:(0,r.Fp)(p.top,p.bottom))}await d({...e,availableWidth:T,availableHeight:L});let A=await a.getDimensions(s.floating);return y!==A.width||x!==A.height?{reset:{rects:!0}}:{}}}},P=function(t){return void 0===t&&(t={}),{name:"hide",options:t,async fn(e){let{rects:n}=e,{strategy:i="referenceHidden",...o}=(0,r.ku)(t,e);switch(i){case"referenceHidden":{let t=u(await l(e,{...o,elementContext:"reference"}),n.reference);return{data:{referenceHiddenOffsets:t,referenceHidden:f(t)}}}case"escaped":{let t=u(await l(e,{...o,altBoundary:!0}),n.floating);return{data:{escapedOffsets:t,escaped:f(t)}}}default:return{}}}}},K=t=>({name:"arrow",options:t,async fn(e){let{x:n,y:i,placement:o,rects:l,platform:u,elements:f,middlewareData:c}=e,{element:a,padding:s=0}=(0,r.ku)(t,e)||{};if(null==a)return{};let d=(0,r.yd)(s),h={x:n,y:i},p=(0,r.Wh)(o),g=(0,r.I4)(p),m=await u.getDimensions(a),w="y"===p,y=w?"clientHeight":"clientWidth",x=l.reference[g]+l.reference[p]-h[p]-l.floating[g],v=h[p]-l.reference[p],b=await (null==u.getOffsetParent?void 0:u.getOffsetParent(a)),R=b?b[y]:0;R&&await (null==u.isElement?void 0:u.isElement(b))||(R=f.floating[y]||l.floating[g]);let k=R/2-m[g]/2-1,F=(0,r.VV)(d[w?"top":"left"],k),L=(0,r.VV)(d[w?"bottom":"right"],k),T=R-m[g]-L,A=R/2-m[g]/2+(x/2-v/2),D=(0,r.uZ)(F,A,T),V=!c.arrow&&null!=(0,r.hp)(o)&&A!==D&&l.reference[g]/2-(A<F?F:L)-m[g]/2<0,E=V?A<F?A-F:A-T:0;return{[p]:h[p]+E,data:{[p]:D,centerOffset:A-D-E,...V&&{alignmentOffset:E}},reset:V}}}),W=function(t){return void 0===t&&(t={}),{name:"inline",options:t,async fn(e){let{placement:n,elements:i,rects:o,platform:l,strategy:u}=e,{padding:f=2,x:a,y:s}=(0,r.ku)(t,e),d=Array.from(await (null==l.getClientRects?void 0:l.getClientRects(i.reference))||[]),h=function(t){let e=t.slice().sort((t,e)=>t.y-e.y),n=[],i=null;for(let t=0;t<e.length;t++){let r=e[t];!i||r.y-i.y>i.height/2?n.push([r]):n[n.length-1].push(r),i=r}return n.map(t=>(0,r.JB)(c(t)))}(d),p=(0,r.JB)(c(d)),g=(0,r.yd)(f),m=await l.getElementRects({reference:{getBoundingClientRect:function(){if(2===h.length&&h[0].left>h[1].right&&null!=a&&null!=s)return h.find(t=>a>t.left-g.left&&a<t.right+g.right&&s>t.top-g.top&&s<t.bottom+g.bottom)||p;if(h.length>=2){if("y"===(0,r.Qq)(n)){let t=h[0],e=h[h.length-1],i="top"===(0,r.k3)(n),o=t.top,l=e.bottom,u=i?t.left:e.left,f=i?t.right:e.right;return{top:o,bottom:l,left:u,right:f,width:f-u,height:l-o,x:u,y:o}}let t="left"===(0,r.k3)(n),e=(0,r.Fp)(...h.map(t=>t.right)),i=(0,r.VV)(...h.map(t=>t.left)),o=h.filter(n=>t?n.left===i:n.right===e),l=o[0].top,u=o[o.length-1].bottom;return{top:l,bottom:u,left:i,right:e,width:e-i,height:u-l,x:i,y:l}}return p}},floating:i.floating,strategy:u});return o.reference.x!==m.reference.x||o.reference.y!==m.reference.y||o.reference.width!==m.reference.width||o.reference.height!==m.reference.height?{reset:{rects:m}}:{}}}},z=function(t){return void 0===t&&(t={}),{options:t,fn(e){let{x:n,y:i,placement:o,rects:l,middlewareData:u}=e,{offset:f=0,mainAxis:c=!0,crossAxis:a=!0}=(0,r.ku)(t,e),s={x:n,y:i},d=(0,r.Qq)(o),h=(0,r.Rn)(d),p=s[h],g=s[d],m=(0,r.ku)(f,e),w="number"==typeof m?{mainAxis:m,crossAxis:0}:{mainAxis:0,crossAxis:0,...m};if(c){let t="y"===h?"height":"width",e=l.reference[h]-l.floating[t]+w.mainAxis,n=l.reference[h]+l.reference[t]-w.mainAxis;p<e?p=e:p>n&&(p=n)}if(a){var y,x;let t="y"===h?"width":"height",e=["top","left"].includes((0,r.k3)(o)),n=l.reference[d]-l.floating[t]+(e&&(null==(y=u.offset)?void 0:y[d])||0)+(e?0:w.crossAxis),i=l.reference[d]+l.reference[t]+(e?0:(null==(x=u.offset)?void 0:x[d])||0)-(e?w.crossAxis:0);g<n?g=n:g>i&&(g=i)}return{[h]:p,[d]:g}}}},J=(t,e,n)=>{let r=new Map,i={platform:L,...n},l={...i.platform,_c:r};return o(t,e,{...i,platform:l})}},10712:function(t,e,n){function r(){return"undefined"!=typeof window}function i(t){return u(t)?(t.nodeName||"").toLowerCase():"#document"}function o(t){var e;return(null==t||null==(e=t.ownerDocument)?void 0:e.defaultView)||window}function l(t){var e;return null==(e=(u(t)?t.ownerDocument:t.document)||window.document)?void 0:e.documentElement}function u(t){return!!r()&&(t instanceof Node||t instanceof o(t).Node)}function f(t){return!!r()&&(t instanceof Element||t instanceof o(t).Element)}function c(t){return!!r()&&(t instanceof HTMLElement||t instanceof o(t).HTMLElement)}function a(t){return!!r()&&"undefined"!=typeof ShadowRoot&&(t instanceof ShadowRoot||t instanceof o(t).ShadowRoot)}function s(t){let{overflow:e,overflowX:n,overflowY:r,display:i}=y(t);return/auto|scroll|overlay|hidden|clip/.test(e+r+n)&&!["inline","contents"].includes(i)}function d(t){return["table","td","th"].includes(i(t))}function h(t){return[":popover-open",":modal"].some(e=>{try{return t.matches(e)}catch(t){return!1}})}function p(t){let e=m(),n=f(t)?y(t):t;return"none"!==n.transform||"none"!==n.perspective||!!n.containerType&&"normal"!==n.containerType||!e&&!!n.backdropFilter&&"none"!==n.backdropFilter||!e&&!!n.filter&&"none"!==n.filter||["transform","perspective","filter"].some(t=>(n.willChange||"").includes(t))||["paint","layout","strict","content"].some(t=>(n.contain||"").includes(t))}function g(t){let e=v(t);for(;c(e)&&!w(e);){if(p(e))return e;if(h(e))break;e=v(e)}return null}function m(){return"undefined"!=typeof CSS&&!!CSS.supports&&CSS.supports("-webkit-backdrop-filter","none")}function w(t){return["html","body","#document"].includes(i(t))}function y(t){return o(t).getComputedStyle(t)}function x(t){return f(t)?{scrollLeft:t.scrollLeft,scrollTop:t.scrollTop}:{scrollLeft:t.scrollX,scrollTop:t.scrollY}}function v(t){if("html"===i(t))return t;let e=t.assignedSlot||t.parentNode||a(t)&&t.host||l(t);return a(e)?e.host:e}function b(t){return t.parent&&Object.getPrototypeOf(t.parent)?t.frameElement:null}n.d(e,{Dx:function(){return y},Jj:function(){return o},Kx:function(){return function t(e,n,r){var i;void 0===n&&(n=[]),void 0===r&&(r=!0);let l=function t(e){let n=v(e);return w(n)?e.ownerDocument?e.ownerDocument.body:e.body:c(n)&&s(n)?n:t(n)}(e),u=l===(null==(i=e.ownerDocument)?void 0:i.body),f=o(l);if(u){let e=b(f);return n.concat(f,f.visualViewport||[],s(l)?l:[],e&&r?t(e):[])}return n.concat(l,t(l,[],r))}},Lw:function(){return x},Ow:function(){return v},Pf:function(){return m},Py:function(){return w},Re:function(){return c},Ze:function(){return d},Zq:function(){return a},ao:function(){return s},gQ:function(){return g},hT:function(){return p},kK:function(){return f},tF:function(){return l},tR:function(){return h},wK:function(){return b},wk:function(){return i}})},4029:function(t,e,n){n.d(e,{Ct:function(){return i},Fp:function(){return l},GW:function(){return f},Go:function(){return R},I4:function(){return w},JB:function(){return T},KX:function(){return k},NM:function(){return u},Qq:function(){return y},Rn:function(){return m},VV:function(){return o},Wh:function(){return x},gy:function(){return b},hp:function(){return g},i8:function(){return v},k3:function(){return p},ku:function(){return h},mA:function(){return r},pw:function(){return F},uZ:function(){return d},yd:function(){return L},ze:function(){return c}});let r=["top","right","bottom","left"],i=r.reduce((t,e)=>t.concat(e,e+"-start",e+"-end"),[]),o=Math.min,l=Math.max,u=Math.round,f=Math.floor,c=t=>({x:t,y:t}),a={left:"right",right:"left",bottom:"top",top:"bottom"},s={start:"end",end:"start"};function d(t,e,n){return l(t,o(e,n))}function h(t,e){return"function"==typeof t?t(e):t}function p(t){return t.split("-")[0]}function g(t){return t.split("-")[1]}function m(t){return"x"===t?"y":"x"}function w(t){return"y"===t?"height":"width"}function y(t){return["top","bottom"].includes(p(t))?"y":"x"}function x(t){return m(y(t))}function v(t,e,n){void 0===n&&(n=!1);let r=g(t),i=x(t),o=w(i),l="x"===i?r===(n?"end":"start")?"right":"left":"start"===r?"bottom":"top";return e.reference[o]>e.floating[o]&&(l=F(l)),[l,F(l)]}function b(t){let e=F(t);return[R(t),e,R(e)]}function R(t){return t.replace(/start|end/g,t=>s[t])}function k(t,e,n,r){let i=g(t),o=function(t,e,n){let r=["left","right"],i=["right","left"];switch(t){case"top":case"bottom":if(n)return e?i:r;return e?r:i;case"left":case"right":return e?["top","bottom"]:["bottom","top"];default:return[]}}(p(t),"start"===n,r);return i&&(o=o.map(t=>t+"-"+i),e&&(o=o.concat(o.map(R)))),o}function F(t){return t.replace(/left|right|bottom|top/g,t=>a[t])}function L(t){return"number"!=typeof t?{top:0,right:0,bottom:0,left:0,...t}:{top:t,right:t,bottom:t,left:t}}function T(t){let{x:e,y:n,width:r,height:i}=t;return{width:r,height:i,top:n,left:e,right:e+r,bottom:n+i,x:e,y:n}}}}]);