import {instrument,type Page} from "@shared/instrument";
import {rect,type Frame} from "@shared/surface";
function sky(page:Page,_pages:Page[],_index:number):Frame{
 if(page.caption!=="SUNRISE"&&page.caption!=="SUNSET")return [];
 const [season,weather]=page.lines;const fall=page.caption==="SUNSET";
 const seasonInk:Record<string,string>={winter:"#96D3F4FF",spring:"#A6D97EFF",summer:"#E5BE73FF",autumn:"#CF8F5AFF"};
 const t=Math.floor(Date.now()/450)%6,y=fall?3+t:8-t;
 const f:Frame=[rect("ground",53,12,18,2,seasonInk[season]||"#84B988FF"),rect("sun",59,y,6,4,"#FFC761FF"),rect("sun-mid",58,y+1,8,2,"#FFC761FF")];
 if(weather!=="clear"){f.push(rect("cloud",56,1,7,2,"#B1C3D2FF"),rect("cloud2",59,0,3,1,"#D9E4ECFF"));}
 if(weather==="rain"||weather==="snow")for(let i=0;i<3;i++)f.push(rect("drop"+i,54+i*6,3+(t+2*i)%7,1,weather==="rain"?2:1,weather==="rain"?"#55A1D8FF":"#EAF1FAFF"));
 return f;
}
instrument({title:"HORIZON HOUR",primary:"Horizon Hour",accent:"#FFC761",cadence:15000,motion:{enabled:false},marks:sky,animationMs:450,setup:"Start companion/serve.py"});
