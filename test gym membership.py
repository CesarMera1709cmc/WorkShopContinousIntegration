"""
Unit Tests for Gym Membership Management System
Tests unitarios para el Sistema de Gestión de Membresías
"""

import unittest
from gym_membership import GymMembership


class TestGymMembership(unittest.TestCase):
    """Clase de tests para el sistema de membresías"""
    
    def setUp(self):
        """Configuración antes de cada test"""
        self.gym = GymMembership()
    
    # Tests para selección de membresía
    def test_select_valid_membership_plan(self):
        """Test: Seleccionar un plan válido"""
        result = self.gym.select_membership_plan("Basic")
        self.assertTrue(result)
        self.assertEqual(self.gym.selected_plan, "Basic")
    
    def test_select_invalid_membership_plan(self):
        """Test: Seleccionar un plan inválido"""
        result = self.gym.select_membership_plan("InvalidPlan")
        self.assertFalse(result)
        self.assertIsNone(self.gym.selected_plan)
    
    def test_all_membership_plans_available(self):
        """Test: Todos los planes deben estar disponibles"""
        plans = ["Basic", "Premium", "Family"]
        for plan in plans:
            self.assertTrue(self.gym.select_membership_plan(plan))
    
    # Tests para características adicionales
    def test_add_valid_additional_feature(self):
        """Test: Agregar característica adicional válida"""
        result = self.gym.add_additional_feature("Personal Training")
        self.assertTrue(result)
        self.assertIn("Personal Training", self.gym.additional_features)
    
    def test_add_invalid_additional_feature(self):
        """Test: Agregar característica adicional inválida"""
        result = self.gym.add_additional_feature("Invalid Feature")
        self.assertFalse(result)
        self.assertNotIn("Invalid Feature", self.gym.additional_features)
    
    def test_add_multiple_additional_features(self):
        """Test: Agregar múltiples características adicionales"""
        self.gym.add_additional_feature("Personal Training")
        self.gym.add_additional_feature("Group Classes")
        self.assertEqual(len(self.gym.additional_features), 2)
    
    # Tests para cálculo de costos base
    def test_calculate_base_cost_basic_plan(self):
        """Test: Calcular costo base del plan Basic"""
        self.gym.select_membership_plan("Basic")
        cost = self.gym.calculate_base_cost()
        self.assertEqual(cost, 50)
    
    def test_calculate_base_cost_premium_plan(self):
        """Test: Calcular costo base del plan Premium"""
        self.gym.select_membership_plan("Premium")
        cost = self.gym.calculate_base_cost()
        self.assertEqual(cost, 100)
    
    def test_calculate_base_cost_family_plan(self):
        """Test: Calcular costo base del plan Family"""
        self.gym.select_membership_plan("Family")
        cost = self.gym.calculate_base_cost()
        self.assertEqual(cost, 150)
    
    def test_calculate_base_cost_no_plan_selected(self):
        """Test: Costo base sin plan seleccionado"""
        cost = self.gym.calculate_base_cost()
        self.assertEqual(cost, 0)
    
    # Tests para costo de características adicionales
    def test_calculate_additional_features_cost_single(self):
        """Test: Calcular costo de una característica adicional"""
        self.gym.add_additional_feature("Personal Training")
        cost = self.gym.calculate_additional_features_cost()
        self.assertEqual(cost, 40)
    
    def test_calculate_additional_features_cost_multiple(self):
        """Test: Calcular costo de múltiples características adicionales"""
        self.gym.add_additional_feature("Personal Training")  # 40
        self.gym.add_additional_feature("Group Classes")      # 25
        cost = self.gym.calculate_additional_features_cost()
        self.assertEqual(cost, 65)
    
    def test_calculate_additional_features_cost_none(self):
        """Test: Calcular costo sin características adicionales"""
        cost = self.gym.calculate_additional_features_cost()
        self.assertEqual(cost, 0)
    
    # Tests para descuento grupal
    def test_group_discount_two_members(self):
        """Test: Descuento grupal con 2 miembros (10%)"""
        self.gym.set_number_of_members(2)
        discount = self.gym.apply_group_discount(100)
        self.assertEqual(discount, 10)
    
    def test_group_discount_one_member(self):
        """Test: Sin descuento grupal con 1 miembro"""
        self.gym.set_number_of_members(1)
        discount = self.gym.apply_group_discount(100)
        self.assertEqual(discount, 0)
    
    def test_group_discount_five_members(self):
        """Test: Descuento grupal con 5 miembros"""
        self.gym.set_number_of_members(5)
        discount = self.gym.apply_group_discount(200)
        self.assertEqual(discount, 20)
    
    def test_set_invalid_number_of_members(self):
        """Test: Número inválido de miembros"""
        result = self.gym.set_number_of_members(0)
        self.assertFalse(result)
    
    # Tests para descuentos especiales
    def test_special_discount_over_400(self):
        """Test: Descuento especial cuando el total excede $400"""
        discount = self.gym.apply_special_offer_discount(450)
        self.assertEqual(discount, 50)
    
    def test_special_discount_over_200(self):
        """Test: Descuento especial cuando el total excede $200"""
        discount = self.gym.apply_special_offer_discount(250)
        self.assertEqual(discount, 20)
    
    def test_special_discount_under_200(self):
        """Test: Sin descuento especial cuando es menor a $200"""
        discount = self.gym.apply_special_offer_discount(150)
        self.assertEqual(discount, 0)
    
    def test_special_discount_exactly_200(self):
        """Test: Sin descuento especial exactamente en $200"""
        discount = self.gym.apply_special_offer_discount(200)
        self.assertEqual(discount, 0)
    
    def test_special_discount_exactly_400(self):
        """Test: Descuento especial exactamente en $400 (debe aplicar $20)"""
        discount = self.gym.apply_special_offer_discount(400)
        self.assertEqual(discount, 20)
    
    # Tests para características premium
    def test_add_valid_premium_feature(self):
        """Test: Agregar característica premium válida"""
        result = self.gym.add_premium_feature("Exclusive Gym Access")
        self.assertTrue(result)
        self.assertIn("Exclusive Gym Access", self.gym.premium_features)
    
    def test_add_invalid_premium_feature(self):
        """Test: Agregar característica premium inválida"""
        result = self.gym.add_premium_feature("Invalid Premium")
        self.assertFalse(result)
    
    def test_calculate_premium_features_cost(self):
        """Test: Calcular costo de características premium"""
        self.gym.add_premium_feature("Exclusive Gym Access")  # 80
        cost = self.gym.calculate_premium_features_cost()
        self.assertEqual(cost, 80)
    
    # Tests para recargo premium
    def test_premium_surcharge_with_premium_features(self):
        """Test: Recargo del 15% con características premium"""
        self.gym.add_premium_feature("Exclusive Gym Access")
        surcharge = self.gym.apply_premium_surcharge(100)
        self.assertEqual(surcharge, 15)
    
    def test_premium_surcharge_without_premium_features(self):
        """Test: Sin recargo premium sin características premium"""
        surcharge = self.gym.apply_premium_surcharge(100)
        self.assertEqual(surcharge, 0)


#Aportaciones de Paul y Juan
