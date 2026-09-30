import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';

import { ToolbarMain } from '../../shared/components/toolbar-main/toolbar-main';
import { SidebarMain } from '../../shared/components/sidebar-main/sidebar-main';
import { BetCard } from '../../shared/components/bet-card/bet-card';

@Component({
  selector: 'app-home',
  imports: [
    RouterOutlet,
    ToolbarMain,
    SidebarMain,
    BetCard
  ],
  templateUrl: './home.html',
  styleUrl: './home.css',
})
export class Home {

  items = [
    {
      id: 1,
      image: 'avestruz.jpeg',
      title: 'Avestruz',
      number: 1,
      dezenas: ['01', '02', '03', '04']
    },
    {
      id: 2,
      image: 'agui.jpeg',
      title: 'Águia',
      number: 2,
      dezenas: ['05', '06', '07', '08']
    },
    {
      id: 3,
      image: 'burro.jpeg',
      title: 'Burro',
      number: 3,
      dezenas: ['09', '10', '11', '12']
    },
    {
      id: 4,
      image: 'borboleta.jpeg',
      title: 'Borboleta',
      number: 4,
      dezenas: ['13', '14', '15', '16']
    },
    {
      id: 5,
      image: 'cachorro.jpeg',
      title: 'Cachorro',
      number: 5,
      dezenas: ['17', '18', '19', '20']
    },
    {
      id: 6,
      image: 'cabra.jpeg',
      title: 'Cabra',
      number: 6,
      dezenas: ['21', '22', '23', '24']
    },
    {
      id: 7,
      image: 'carneiro.jpeg',
      title: 'Carneiro',
      number: 7,
      dezenas: ['25', '26', '27', '28']
    },
    {
      id: 8,
      image: 'camelo.jpeg',
      title: 'Camelo',
      number: 8,
      dezenas: ['29', '30', '31', '32']
    },
    {
      id: 9,
      image: 'cobra.jpeg',
      title: 'Cobra',
      number: 9,
      dezenas: ['33', '34', '35', '36']
    },
    {
      id: 10,
      image: 'coelho.jpeg',
      title: 'Coelho',
      number: 10,
      dezenas: ['37', '38', '39', '40']
    },
    {
      id: 11,
      image: 'cavalo.jpg',
      title: 'Cavalo',
      number: 11,
      dezenas: ['41', '42', '43', '44']
    },
    {
      id: 12,
      image: 'elefante.jpg',
      title: 'Elefante',
      number: 12,
      dezenas: ['45', '46', '47', '48']
    },
    {
      id: 13,
      image: 'galo.jpeg',
      title: 'Galo',
      number: 13,
      dezenas: ['49', '50', '51', '52']
    },
    {
      id: 14,
      image: 'gato.jpeg',
      title: 'Gato',
      number: 14,
      dezenas: ['53', '54', '55', '56']
    },
    {
      id: 15,
      image: 'jacare.jpg',
      title: 'Jacaré',
      number: 15,
      dezenas: ['57', '58', '59', '60']
    },
    {
      id: 16,
      image: 'leao.jpeg',
      title: 'Leão',
      number: 16,
      dezenas: ['61', '62', '63', '64']
    },
    {
      id: 17,
      image: 'macaco.jpeg',
      title: 'Macaco',
      number: 17,
      dezenas: ['65', '66', '67', '68']
    },
    {
      id: 18,
      image: 'porco.jpg',
      title: 'Porco',
      number: 18,
      dezenas: ['69', '70', '71', '72']
    },
    {
      id: 19,
      image: 'pavao.jpeg',
      title: 'Pavão',
      number: 19,
      dezenas: ['73', '74', '75', '76']
    },
    {
      id: 20,
      image: 'peru.jpg',
      title: 'Peru',
      number: 20,
      dezenas: ['77', '78', '79', '80']
    },
    {
      id: 21,
      image: 'touro.jpg',
      title: 'Touro',
      number: 21,
      dezenas: ['81', '82', '83', '84']
    },
    {
      id: 22,
      image: 'tigre.jpg',
      title: 'Tigre',
      number: 22,
      dezenas: ['85', '86', '87', '88']
    },
    {
      id: 23,
      image: 'urso.jpg',
      title: 'Urso',
      number: 23,
      dezenas: ['89', '90', '91', '92']
    },
    {
      id: 24,
      image: 'veado.jpeg',
      title: 'Veado',
      number: 24,
      dezenas: ['93', '94', '95', '96']
    },
    {
      id: 25,
      image: 'vaca.jpeg',
      title: 'Vaca',
      number: 25,
      dezenas: ['97', '98', '99', '00']
    }
  ];

}