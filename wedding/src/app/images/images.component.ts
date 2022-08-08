import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-images',
  templateUrl: './images.component.html',
  styleUrls: ['./images.component.scss']
})
export class ImagesComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {

    new Promise(resolve =>
      {
          const node = document.createElement('script');
          node.src = 'https://cdn.jsdelivr.net/npm/publicalbum@latest/embed-ui.min.js'; // put there your js file location
          node.type = 'text/javascript';
          node.async = true;
          node.charset = 'utf-8';
          document.getElementsByTagName('head')[0].appendChild(node);
      })

  }

}
